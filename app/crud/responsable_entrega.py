from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models import ResponsableEntrega
from app.schemas import ResponsableEntregaCreate, ResponsableEntregaUpdate

# Crear
def create(db: Session, data: ResponsableEntregaCreate):
    nuevo = ResponsableEntrega(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Obtener todos con filtros opcionales
def get_filtered(db: Session, empleado_id=None, recibe=None, entrega=None):
    query = db.query(ResponsableEntrega)

    if empleado_id is not None:
        query = query.filter(ResponsableEntrega.EmpleadoId == empleado_id)
    if recibe is not None:
        query = query.filter(ResponsableEntrega.Recibe.ilike(f"%{recibe}%"))
    if entrega is not None:
        query = query.filter(ResponsableEntrega.Entrega.ilike(f"%{entrega}%"))

    return query.all()

# Obtener por ID
def get_by_id(db: Session, id: int):
    return db.query(ResponsableEntrega).filter(ResponsableEntrega.Id == id).first()

# Actualizar
def update(db: Session, id: int, data: ResponsableEntregaUpdate):
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