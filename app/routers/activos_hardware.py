from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from app.db.db import get_db
from app.schemas import ActivoHardwareCreate, ActivoHardwareUpdate, ActivoHardwareOut
from app.crud import activos_hardware

router = APIRouter(prefix="/hardware", tags=["Activos Hardware"])

# Crear un activo
@router.post("/", response_model=ActivoHardwareOut)
def create_activo(data: ActivoHardwareCreate, db: Session = Depends(get_db)):
    return activos_hardware.create(db, data)

# Obtener todos los activos con filtros dinámicos
@router.get("/", response_model=List[ActivoHardwareOut])
def get_all_activos(
    tipo: Optional[str] = Query(None),
    marca: Optional[str] = Query(None),
    empleado_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    return activos_hardware.get_all(db, tipo=tipo, marca=marca, empleado_id=empleado_id)

# Obtener un activo por su ID
@router.get("/{id}", response_model=ActivoHardwareOut)
def get_activo_by_id(id: int, db: Session = Depends(get_db)):
    activo = activos_hardware.get_by_id(db, id)
    if not activo:
        raise HTTPException(status_code=404, detail="Activo no encontrado")
    return activo

# Obtener todos los activos asignados a un empleado específico
@router.get("/empleado/{empleado_id}", response_model=List[ActivoHardwareOut])
def get_activos_by_empleado(empleado_id: int, db: Session = Depends(get_db)):
    return activos_hardware.get_by_empleado_id(db, empleado_id)

# Actualizar un activo por ID
@router.put("/{id}", response_model=ActivoHardwareOut)
def update_activo(id: int, data: ActivoHardwareUpdate, db: Session = Depends(get_db)):
    actualizado = activos_hardware.update(db, id, data)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Activo no encontrado")
    return actualizado

# Eliminar un activo por ID
@router.delete("/{id}")
def delete_activo(id: int, db: Session = Depends(get_db)):
    eliminado = activos_hardware.delete(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Activo no encontrado")
    return {"message": "Activo eliminado correctamente"}
