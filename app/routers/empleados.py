from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas import EmpleadoCreate, EmpleadoUpdate, EmpleadoOut
from app.crud import empleados

router = APIRouter(prefix="/empleados", tags=["Empleados"])

@router.get("/", response_model=list[EmpleadoOut])
def get_all_empleados(db: Session = Depends(get_db)):
    return empleados.get_all(db)

@router.post("/", response_model=EmpleadoOut)
def create_empleado(data: EmpleadoCreate, db: Session = Depends(get_db)):
    return empleados.create(db, data)

@router.put("/{empleado_id}", response_model=EmpleadoOut)
def update_empleado(empleado_id: int, data: EmpleadoUpdate, db: Session = Depends(get_db)):
    updated = empleados.update(db, empleado_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return updated

@router.delete("/{empleado_id}")
def delete_empleado(empleado_id: int, db: Session = Depends(get_db)):
    deleted = empleados.delete(db, empleado_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return {"message": "Empleado eliminado correctamente"}
