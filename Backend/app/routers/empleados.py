# app/routers/empleados.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Backend.app.Db import db
from Backend.app.schemas import schemas
from app import crud

router = APIRouter(prefix="/empleados", tags=["Empleados"])

@router.get("/", response_model=list[schemas.Empleado])
def listar_empleados(db_session: Session = Depends(db.get_db)):
    return crud.get_empleados(db_session)

@router.get("/{empleado_id}", response_model=schemas.Empleado)
def obtener_empleado(empleado_id: int, db_session: Session = Depends(db.get_db)):
    empleado = crud.get_empleado(db_session, empleado_id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

@router.post("/", response_model=schemas.Empleado)
def crear_empleado(empleado: schemas.EmpleadoCreate, db_session: Session = Depends(db.get_db)):
    return crud.create_empleado(db_session, empleado)

@router.put("/{empleado_id}", response_model=schemas.Empleado)
def actualizar_empleado(empleado_id: int, empleado: schemas.EmpleadoCreate, db_session: Session = Depends(db.get_db)):
    return crud.update_empleado(db_session, empleado_id, empleado)

@router.delete("/{empleado_id}")
def eliminar_empleado(empleado_id: int, db_session: Session = Depends(db.get_db)):
    if not crud.delete_empleado(db_session, empleado_id):
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return {"mensaje": "Empleado eliminado exitosamente"}