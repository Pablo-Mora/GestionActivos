from docxtpl import DocxTemplate
import os
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.models import Empleado


def get_empleado_con_todo(db: Session, identificacion: str):
    empleado = db.query(Empleado).filter(Empleado.Identificacion == identificacion).first()
    if not empleado:
        return None

    datos_empleado = {
        "FECHA": empleado.Fecha.strftime("%d/%m/%Y") if empleado.Fecha else "",
        "CLASE_ACTA": empleado.ClaseActa,
        "NOMBRE": empleado.Nombre,
        "IDENTIFICACION": empleado.Identificacion,
        "CARGO": empleado.Cargo,
        "DEPENDENCIA": empleado.Dependencia,
        "UBICACION": empleado.UbicacionOficina,
    }

    hardware_items = [
        {
            "NOMBRE": h.TipoHardware,
            "CANTIDAD": h.Cantidad,
            "MARCA": h.Marca,
            "MODELO": h.Modelo,
            "SERIAL": h.Serial,
            "OBS": h.Observaciones or ""
        }
        for h in empleado.activos_hardware
    ]

    licencias_items = [
        {
            "NOMBRE": l.NombreLicencia,
            "LICENCIA": l.Usuario,
            "OBS": "Obligatorio" if l.ObligadoCambio else "No"
        }
        for l in empleado.licencias_software
    ]

    accesos_items = [
        {
            "URL": a.URL,
            "USUARIO": a.Usuario,
            "CONTRASENA": a.Contrasena,
            "OBS": "Obligatorio" if a.ObligadoCambio else "No"
        }
        for a in empleado.accesos_web
    ]

    responsable = empleado.responsables_entrega[0] if empleado.responsables_entrega else None
    datos_responsable = {
        "ENTREGA": responsable.Entrega if responsable else "",
        "RECIBE": responsable.Recibe if responsable else "",
        "ROL_ENTREGA": responsable.RolEntrega if responsable else "",
        "ROL_RECIBE": responsable.RolRecibe if responsable else "",
    }

    aprobacion = empleado.aprobaciones[0] if empleado.aprobaciones else None
    datos_aprobacion = {
        "APROBADO_POR": aprobacion.AprobadoPor if aprobacion else "",
        "CARGO_APROBADOR": aprobacion.CargoAprobador if aprobacion else "",
    }

    contexto = {
        **datos_empleado,
        **datos_responsable,
        **datos_aprobacion,
        "hardware_items": hardware_items,
        "licencias_items": licencias_items,
        "accesos_items": accesos_items,
    }

    return contexto


def generar_documento_word(contexto: dict, output_path: str = None):
    plantilla_path = os.path.join("app", "templates", "plantilla_activos.docx")
    doc = DocxTemplate(plantilla_path)
    doc.render(contexto)

    clase_acta = contexto.get("CLASE_ACTA", "ACTA").upper().replace(" ", "_")
    nombre_empleado = contexto.get("NOMBRE", "EMPLEADO").upper().replace(" ", "_")
    fecha = datetime.now().strftime("%d-%m-%y")

    nombre_archivo = f"ACTA_{clase_acta}_FECHA_{fecha}_{nombre_empleado}.docx"

    if not output_path:
        output_path = os.path.join("app", "static", "downloads", nombre_archivo)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)

    return output_path
