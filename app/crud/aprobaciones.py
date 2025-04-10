from sqlalchemy.orm import Session
from app.models import Aprobacion
from app.schemas import AprobacionCreate, AprobacionUpdate

# Crear
def create(db: Session, data: AprobacionCreate):
    nueva = Aprobacion(**data.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

# Obtener todos con filtros dinámicos
def get_filtered(db: Session, empleado_id=None, aprobado_por=None):
    query = db.query(Aprobacion)

    if empleado_id is not None:
        query = query.filter(Aprobacion.EmpleadoId == empleado_id)
    if aprobado_por is not None:
        query = query.filter(Aprobacion.AprobadoPor.ilike(f"%{aprobado_por}%"))

    return query.all()

# Obtener por ID
def get_by_id(db: Session, id: int):
    return db.query(Aprobacion).filter(Aprobacion.Id == id).first()

# Actualizar
def update(db: Session, id: int, data: AprobacionUpdate):
    item = get_by_id(db, id)
    if not item:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

# Eliminar
def delete(db: Session, id: int):
    item = get_by_id(db, id)
    if not item:
        return None
    db.delete(item)
    db.commit()
    return item
