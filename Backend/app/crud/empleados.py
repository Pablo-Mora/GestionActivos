from sqlalchemy.orm import Session
from Backend.app.models.models import Empleado
from Backend.app.schemas.schemas import EmpleadoCreate, EmpleadoUpdate

# Crear un empleado
def create_empleado(db: Session, empleado: EmpleadoCreate):
    db_empleado = Empleado(**empleado.dict())
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

# Obtener todos los empleados
def get_empleados(db: Session):
    return db.query(Empleado).all()

# Obtener un empleado por ID
def get_empleado(db: Session, empleado_id: int):
    return db.query(Empleado).filter(Empleado.Id == empleado_id).first()

# Actualizar un empleado
def update_empleado(db: Session, empleado_id: int, empleado_data: EmpleadoUpdate):
    empleado = db.query(Empleado).filter(Empleado.Id == empleado_id).first()
    if empleado:
        for key, value in empleado_data.dict(exclude_unset=True).items():
            setattr(empleado, key, value)
        db.commit()
        db.refresh(empleado)
    return empleado

# Eliminar un empleado
def delete_empleado(db: Session, empleado_id: int):
    empleado = db.query(Empleado).filter(Empleado.Id == empleado_id).first()
    if empleado:
        db.delete(empleado)
        db.commit()
    return empleado