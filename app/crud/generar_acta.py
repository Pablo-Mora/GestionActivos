from sqlalchemy.orm import Session
from app.models.models import Empleado, ActivoHardware, LicenciaSoftware, AccesoWeb, ResponsableEntrega, Aprobacion


def get_empleado_con_todo(db: Session, identificacion: str):
    empleado = db.query(Empleado).filter(Empleado.Identificacion == identificacion).first()
    if not empleado:
        return None

    # Diccionario de datos básicos del empleado
    datos_empleado = {
        "FECHA": empleado.Fecha.strftime("%d/%m/%Y") if empleado.Fecha else "",
        "CLASE_ACTA": empleado.ClaseActa,
        "NOMBRE": empleado.Nombre,
        "IDENTIFICACION": empleado.Identificacion,
        "CARGO": empleado.Cargo,
        "DEPENDENCIA": empleado.Dependencia,
        "UBICACION": empleado.UbicacionOficina,
    }

    # Hardware
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

    # Licencias
    licencias_items = [
        {
            "NOMBRE": l.NombreLicencia,
            "LICENCIA": l.Usuario,
            "OBS": "Obligatorio" if l.ObligadoCambio else "No"
        }
        for l in empleado.licencias_software
    ]

    # Accesos Web (si lo necesitas en el acta)
    accesos_items = [
        {
            "URL": a.URL,
            "USUARIO": a.Usuario,
            "CONTRASENA": a.Contrasena,
            "OBS": "Obligatorio" if a.ObligadoCambio else "No"
        }
        for a in empleado.accesos_web
    ]

    # Responsables
    responsable = empleado.responsables_entrega[0] if empleado.responsables_entrega else None
    datos_responsable = {
        "ENTREGA": responsable.Entrega if responsable else "",
        "RECIBE": responsable.Recibe if responsable else "",
        "ROL_ENTREGA": responsable.RolEntrega if responsable else "",
        "ROL_RECIBE": responsable.RolRecibe if responsable else "",
    }

    # Aprobaciones
    aprobacion = empleado.aprobaciones[0] if empleado.aprobaciones else None
    datos_aprobacion = {
        "APROBADO_POR": aprobacion.AprobadoPor if aprobacion else "",
        "CARGO_APROBADOR": aprobacion.CargoAprobador if aprobacion else "",
    }

    # Unificar todo para enviar al render de Word
    contexto = {
        **datos_empleado,
        **datos_responsable,
        **datos_aprobacion,
        "hardware_items": hardware_items,
        "licencias_items": licencias_items,
        "accesos_items": accesos_items,  # si lo usas en el documento
    }

    return contexto