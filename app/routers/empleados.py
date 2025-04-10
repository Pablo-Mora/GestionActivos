from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas import (
    EmpleadoCreate, EmpleadoUpdate, EmpleadoOut, EmpleadoDetalleOut
)
from app.crud import empleados

router = APIRouter(prefix="/empleados", tags=["Empleados"])

# Crear empleado
@router.post("/", response_model=EmpleadoOut)
def create_empleado(data: EmpleadoCreate, db: Session = Depends(get_db)):
    return empleados.create(db, data)

# Obtener todos o filtrar por nombre, identificación, cargo
@router.get("/", response_model=list[EmpleadoOut])
def get_empleados(
    nombre: str = Query(None),
    identificacion: str = Query(None),
    cargo: str = Query(None),
    db: Session = Depends(get_db)
):
    if nombre or identificacion or cargo:
        return empleados.get_filtered(db, nombre, identificacion, cargo)
    return empleados.get_all(db)

# Obtener empleado por ID
@router.get("/{empleado_id}", response_model=EmpleadoOut)
def get_empleado_by_id(empleado_id: int, db: Session = Depends(get_db)):
    empleado = empleados.get_by_id(db, empleado_id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

# Obtener empleado detallado por identificación
@router.get("/detalle/{identificacion}", response_model=EmpleadoDetalleOut)
def get_empleado_detalle(identificacion: str, db: Session = Depends(get_db)):
    empleado = empleados.get_detalle_by_identificacion(db, identificacion)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

# Actualizar empleado
@router.put("/{empleado_id}", response_model=EmpleadoOut)
def update_empleado(empleado_id: int, data: EmpleadoUpdate, db: Session = Depends(get_db)):
    updated = empleados.update(db, empleado_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return updated

# Eliminar empleado
@router.delete("/{empleado_id}")
def delete_empleado(empleado_id: int, db: Session = Depends(get_db)):
    deleted = empleados.delete(db, empleado_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return {"message": "Empleado eliminado correctamente"}
