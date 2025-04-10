from sqlalchemy.orm import Session
from app.models.models import LicenciaSoftware
from app.schemas import LicenciaSoftwareCreate, LicenciaSoftwareUpdate

# Crear una licencia
def create(db: Session, data: LicenciaSoftwareCreate):
    nueva_licencia = LicenciaSoftware(**data.model_dump())
    db.add(nueva_licencia)
    db.commit()
    db.refresh(nueva_licencia)
    return nueva_licencia

# Obtener todas con filtros dinámicos
def get_all(db: Session, nombre: str = None, usuario: str = None, empleado_id: int = None):
    query = db.query(LicenciaSoftware)
    if nombre:
        query = query.filter(LicenciaSoftware.NombreLicencia.ilike(f"%{nombre}%"))
    if usuario:
        query = query.filter(LicenciaSoftware.Usuario.ilike(f"%{usuario}%"))
    if empleado_id:
        query = query.filter(LicenciaSoftware.EmpleadoId == empleado_id)
    return query.all()

# Obtener por ID
def get_by_id(db: Session, licencia_id: int):
    return db.query(LicenciaSoftware).filter(LicenciaSoftware.Id == licencia_id).first()

# Obtener todas por empleado
def get_by_empleado_id(db: Session, empleado_id: int):
    return db.query(LicenciaSoftware).filter(LicenciaSoftware.EmpleadoId == empleado_id).all()

# Actualizar licencia
def update(db: Session, licencia_id: int, data: LicenciaSoftwareUpdate):
    licencia = db.query(LicenciaSoftware).filter(LicenciaSoftware.Id == licencia_id).first()
    if licencia:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(licencia, key, value)
        db.commit()
        db.refresh(licencia)
    return licencia

# Eliminar licencia
def delete(db: Session, licencia_id: int):
    licencia = db.query(LicenciaSoftware).filter(LicenciaSoftware.Id == licencia_id).first()
    if licencia:
        db.delete(licencia)
        db.commit()
    return licencia
