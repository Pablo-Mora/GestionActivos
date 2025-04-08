from sqlalchemy.orm import Session
from app.models import LicenciaSoftware
from app.schemas import LicenciaSoftwareCreate, LicenciaSoftwareUpdate

def get_licencias_software(db: Session):
    return db.query(LicenciaSoftware).all()

def get_licencia_software_by_id(db: Session, id: int):
    return db.query(LicenciaSoftware).filter(LicenciaSoftware.Id == id).first()

def create_licencia_software(db: Session, licencia: LicenciaSoftwareCreate):
    db_licencia = LicenciaSoftware(**licencia.dict())
    db.add(db_licencia)
    db.commit()
    db.refresh(db_licencia)
    return db_licencia

def update_licencia_software(db: Session, id: int, licencia: LicenciaSoftwareUpdate):
    db_licencia = db.query(LicenciaSoftware).filter(LicenciaSoftware.Id == id).first()
    if not db_licencia:
        return None
    for field, value in licencia.dict(exclude_unset=True).items():
        setattr(db_licencia, field, value)
    db.commit()
    db.refresh(db_licencia)
    return db_licencia

def delete_licencia_software(db: Session, id: int):
    db_licencia = db.query(LicenciaSoftware).filter(LicenciaSoftware.Id == id).first()
    if not db_licencia:
        return False
    db.delete(db_licencia)
    db.commit()
    return True