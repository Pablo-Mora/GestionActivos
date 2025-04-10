from sqlalchemy.orm import Session
from app.models import AccesoWeb
from app.schemas import AccesoWebCreate, AccesoWebUpdate
from typing import List, Optional

def get_all(db: Session) -> List[AccesoWeb]:
    return db.query(AccesoWeb).all()

def get_by_id(db: Session, id: int) -> Optional[AccesoWeb]:
    return db.query(AccesoWeb).filter(AccesoWeb.Id == id).first()

def get_filtered(db: Session, empleado_id: Optional[int] = None, url: Optional[str] = None) -> List[AccesoWeb]:
    query = db.query(AccesoWeb)
    if empleado_id is not None:
        query = query.filter(AccesoWeb.EmpleadoId == empleado_id)
    if url:
        query = query.filter(AccesoWeb.URL.ilike(f"%{url}%"))
    return query.all()

def create(db: Session, data: AccesoWebCreate) -> AccesoWeb:
    acceso = AccesoWeb(**data.model_dump())
    db.add(acceso)
    db.commit()
    db.refresh(acceso)
    return acceso

def update(db: Session, id: int, data: AccesoWebUpdate) -> Optional[AccesoWeb]:
    acceso = db.query(AccesoWeb).filter(AccesoWeb.Id == id).first()
    if not acceso:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(acceso, field, value)
    db.commit()
    db.refresh(acceso)
    return acceso

def delete(db: Session, id: int) -> bool:
    acceso = db.query(AccesoWeb).filter(AccesoWeb.Id == id).first()
    if acceso:
        db.delete(acceso)
        db.commit()
        return True
    return False
