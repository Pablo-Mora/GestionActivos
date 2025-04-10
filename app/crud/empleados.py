from sqlalchemy.orm import Session, joinedload
from app.models.models import Empleado
from app.schemas import EmpleadoCreate, EmpleadoUpdate

# Crear un empleado
def create(db: Session, empleado: EmpleadoCreate):
    nuevo_empleado = Empleado(**empleado.model_dump())
    db.add(nuevo_empleado)
    db.commit()
    db.refresh(nuevo_empleado)
    return nuevo_empleado

# Obtener todos los empleados
def get_all(db: Session):
    return db.query(Empleado).all()

# Obtener empleados con filtros dinámicos
def get_filtered(db: Session, nombre=None, identificacion=None, cargo=None):
    query = db.query(Empleado)
    if nombre:
        query = query.filter(Empleado.Nombre.ilike(f"%{nombre}%"))
    if identificacion:
        query = query.filter(Empleado.Identificacion.ilike(f"%{identificacion}%"))
    if cargo:
        query = query.filter(Empleado.Cargo.ilike(f"%{cargo}%"))
    return query.all()

# Obtener detalle de un empleado por número de identificación
def get_detalle_by_identificacion(db: Session, identificacion: str):
    return db.query(Empleado)\
        .options(
            joinedload(Empleado.activos_hardware),
            joinedload(Empleado.licencias_software),
            joinedload(Empleado.accesos_web),
            joinedload(Empleado.responsables_entrega),
            joinedload(Empleado.aprobaciones)
        )\
        .filter(Empleado.Identificacion == identificacion)\
        .first()

# Actualizar un empleado
def update(db: Session, empleado_id: int, data: EmpleadoUpdate):
    empleado = db.query(Empleado).filter(Empleado.Id == empleado_id).first()
    if not empleado:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(empleado, key, value)
    db.commit()
    db.refresh(empleado)
    return empleado

# Eliminar un empleado
def delete(db: Session, empleado_id: int):
    empleado = db.query(Empleado).filter(Empleado.Id == empleado_id).first()
    if not empleado:
        return None
    db.delete(empleado)
    db.commit()
    return empleado
