from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Backend.app.Db import db
from Backend.app.schemas.schemas import ActivoHardwareCreate, ActivoHardwareUpdate
from app import crud

router = APIRouter(
    prefix="/activos_hardware",
    tags=["Activos Hardware"]
)

@router.get("/")
def get_activos_hardware(db_session: Session = Depends(db.get_db)):
    return crud.get_activos_hardware(db_session)

@router.get("/{id}")
def get_activo_hardware_by_id(id: int, db_session: Session = Depends(db.get_db)):
    activo = crud.get_activo_hardware_by_id(db_session, id)
    if not activo:
        raise HTTPException(status_code=404, detail="Activo de hardware no encontrado")
    return activo

@router.post("/")
def create_activo_hardware(activo: ActivoHardwareCreate, db_session: Session = Depends(db.get_db)):
    return crud.create_activo_hardware(db_session, activo)

@router.put("/{id}")
def update_activo_hardware(id: int, activo: ActivoHardwareUpdate, db_session: Session = Depends(db.get_db)):
    updated = crud.update_activo_hardware(db_session, id, activo)
    if not updated:
        raise HTTPException(status_code=404, detail="Activo de hardware no encontrado")
    return {"message": "Activo actualizado correctamente"}

@router.delete("/{id}")
def delete_activo_hardware(id: int, db_session: Session = Depends(db.get_db)):
    deleted = crud.delete_activo_hardware(db_session, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Activo de hardware no encontrado")
    return {"message": "Activo eliminado correctamente"}