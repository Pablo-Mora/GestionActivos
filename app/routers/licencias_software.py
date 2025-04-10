from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from app.db.db import get_db
from app.schemas import LicenciaSoftwareCreate, LicenciaSoftwareUpdate, LicenciaSoftwareOut
from app.crud import licencias_software

router = APIRouter(prefix="/licencias", tags=["Licencias Software"])

# Crear una licencia
@router.post("/", response_model=LicenciaSoftwareOut)
def create_licencia(data: LicenciaSoftwareCreate, db: Session = Depends(get_db)):
    return licencias_software.create(db, data)

# Obtener todas las licencias con filtros dinámicos
@router.get("/", response_model=List[LicenciaSoftwareOut])
def get_all_licencias(
    nombre: Optional[str] = Query(None),
    usuario: Optional[str] = Query(None),
    empleado_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    return licencias_software.get_all(db, nombre=nombre, usuario=usuario, empleado_id=empleado_id)

# Obtener una licencia por ID
@router.get("/{id}", response_model=LicenciaSoftwareOut)
def get_licencia_by_id(id: int, db: Session = Depends(get_db)):
    licencia = licencias_software.get_by_id(db, id)
    if not licencia:
        raise HTTPException(status_code=404, detail="Licencia no encontrada")
    return licencia

# Obtener licencias por EmpleadoId
@router.get("/empleado/{empleado_id}", response_model=List[LicenciaSoftwareOut])
def get_licencias_by_empleado(empleado_id: int, db: Session = Depends(get_db)):
    return licencias_software.get_by_empleado_id(db, empleado_id)

# Actualizar una licencia
@router.put("/{id}", response_model=LicenciaSoftwareOut)
def update_licencia(id: int, data: LicenciaSoftwareUpdate, db: Session = Depends(get_db)):
    actualizada = licencias_software.update(db, id, data)
    if not actualizada:
        raise HTTPException(status_code=404, detail="Licencia no encontrada")
    return actualizada

# Eliminar una licencia
@router.delete("/{id}")
def delete_licencia(id: int, db: Session = Depends(get_db)):
    eliminada = licencias_software.delete(db, id)
    if not eliminada:
        raise HTTPException(status_code=404, detail="Licencia no encontrada")
    return {"message": "Licencia eliminada correctamente"}
