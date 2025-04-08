from sqlalchemy.orm import Session
from app.models import Empleado, ActivoHardware, LicenciaSoftware

def get_empleado_con_todo(db: Session, empleado_id: int):
    empleado = db.query(Empleado).filter(Empleado.Id == empleado_id).first()
    if not empleado:
        return None

    hardware = db.query(ActivoHardware).filter(ActivoHardware.EmpleadoId == empleado_id).all()
    licencias = db.query(LicenciaSoftware).filter(LicenciaSoftware.EmpleadoId == empleado_id).all()

    hardware_items = [
        {
            "NOMBRE": h.TipoHardware,
            "CANTIDAD": h.Cantidad,
            "MARCA": h.Marca,
            "MODELO": h.Modelo,
            "SERIAL": h.Serial,
            "OBS": h.Observaciones or ""
        }
        for h in hardware
    ]

    licencias_items = [
        {
            "NOMBRE": l.NombreLicencia,
            "LICENCIA": l.Usuario,
            "OBS": "Obligatorio" if l.ObligadoCambio else "No"
        }
        for l in licencias
    ]

    return {
        "empleado": empleado,
        "hardware_items": hardware_items,
        "licencias_items": licencias_items
    }
