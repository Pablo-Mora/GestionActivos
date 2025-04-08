from sqlalchemy.orm import Session
from Backend.app.models.models import ActivoHardware
from Backend.app.schemas.schemas import ActivoHardwareCreate, ActivoHardwareUpdate

# Crear un activo de hardware
def create_activo_hardware(db: Session, activo: ActivoHardwareCreate):
    db_activo = ActivoHardware(**activo.dict())
    db.add(db_activo)
    db.commit()
    db.refresh(db_activo)
    return db_activo

# Obtener todos los activos de hardware
def get_activos_hardware(db: Session):
    return db.query(ActivoHardware).all()

# Obtener un activo de hardware por ID
def get_activo_hardware(db: Session, activo_id: int):
    return db.query(ActivoHardware).filter(ActivoHardware.Id == activo_id).first()

# Actualizar un activo de hardware
def update_activo_hardware(db: Session, activo_id: int, activo_data: ActivoHardwareUpdate):
    activo = db.query(ActivoHardware).filter(ActivoHardware.Id == activo_id).first()
    if activo:
        for key, value in activo_data.dict(exclude_unset=True).items():
            setattr(activo, key, value)
        db.commit()
        db.refresh(activo)
    return activo

# Eliminar un activo de hardware
def delete_activo_hardware(db: Session, activo_id: int):
    activo = db.query(ActivoHardware).filter(ActivoHardware.Id == activo_id).first()
    if activo:
        db.delete(activo)
        db.commit()
    return activo

from sqlalchemy.orm import Session
from Backend.app.models.models import LicenciaSoftware
from Backend.app.schemas.schemas import LicenciaSoftwareCreate, LicenciaSoftwareUpdate

# Crear una nueva licencia
def create_licencia_software(db: Session, licencia: LicenciaSoftwareCreate):
    db_licencia = LicenciaSoftware(**licencia.dict())
    db.add(db_licencia)
    db.commit()
    db.refresh(db_licencia)
    return db_licencia

# Obtener todas las licencias
def get_licencias_software(db: Session):
    return db.query(LicenciaSoftware).all()

# Obtener una licencia por ID
def get_licencia_software(db: Session, licencia_id: int):
    return db.query(LicenciaSoftware).filter(LicenciaSoftware.Id == licencia_id).first()

# Actualizar una licencia
def update_licencia_software(db: Session, licencia_id: int, licencia_data: LicenciaSoftwareUpdate):
    licencia = db.query(LicenciaSoftware).filter(LicenciaSoftware.Id == licencia_id).first()
    if licencia:
        for key, value in licencia_data.dict(exclude_unset=True).items():
            setattr(licencia, key, value)
        db.commit()
        db.refresh(licencia)
    return licencia

# Eliminar una licencia
def delete_licencia_software(db: Session, licencia_id: int):
    licencia = db.query(LicenciaSoftware).filter(LicenciaSoftware.Id == licencia_id).first()
    if licencia:
        db.delete(licencia)
        db.commit()
    return licencia
