from sqlalchemy.orm import Session
from app.models.models import ActivoHardware
from app.schemas import ActivoHardwareCreate, ActivoHardwareUpdate
from typing import Optional

def create(db: Session, data: ActivoHardwareCreate):
    nuevo = ActivoHardware(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_all(db: Session, tipo: Optional[str] = None, marca: Optional[str] = None, empleado_id: Optional[int] = None):
    query = db.query(ActivoHardware)
    if tipo:
        query = query.filter(ActivoHardware.TipoHardware.ilike(f"%{tipo}%"))
    if marca:
        query = query.filter(ActivoHardware.Marca.ilike(f"%{marca}%"))
    if empleado_id:
        query = query.filter(ActivoHardware.EmpleadoId == empleado_id)
    return query.all()

def get_by_id(db: Session, id: int):
    return db.query(ActivoHardware).filter(ActivoHardware.Id == id).first()

def get_by_empleado_id(db: Session, empleado_id: int):
    return db.query(ActivoHardware).filter(ActivoHardware.EmpleadoId == empleado_id).all()

def update(db: Session, id: int, data: ActivoHardwareUpdate):
    activo = db.query(ActivoHardware).filter(ActivoHardware.Id == id).first()
    if not activo:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(activo, key, value)
    db.commit()
    db.refresh(activo)
    return activo

def delete(db: Session, id: int):
    activo = db.query(ActivoHardware).filter(ActivoHardware.Id == id).first()
    if activo:
        db.delete(activo)
        db.commit()
    return activo
