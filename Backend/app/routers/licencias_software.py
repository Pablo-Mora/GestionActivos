from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Backend.app.Db import db
from Backend.app.schemas.schemas import LicenciaSoftwareCreate, LicenciaSoftwareUpdate
from app import crud

router = APIRouter(
    prefix="/licencias_software",
    tags=["Licencias Software"]
)

@router.get("/")
def get_licencias_software(db_session: Session = Depends(db.get_db)):
    return crud.get_licencias_software(db_session)

@router.get("/{id}")
def get_licencia_software_by_id(id: int, db_session: Session = Depends(db.get_db)):
    licencia = crud.get_licencia_software_by_id(db_session, id)
    if not licencia:
        raise HTTPException(status_code=404, detail="Licencia no encontrada")
    return licencia

@router.post("/")
def create_licencia_software(licencia: LicenciaSoftwareCreate, db_session: Session = Depends(db.get_db)):
    return crud.create_licencia_software(db_session, licencia)

@router.put("/{id}")
def update_licencia_software(id: int, licencia: LicenciaSoftwareUpdate, db_session: Session = Depends(db.get_db)):
    updated = crud.update_licencia_software(db_session, id, licencia)
    if not updated:
        raise HTTPException(status_code=404, detail="Licencia no encontrada")
    return {"message": "Licencia actualizada correctamente"}

@router.delete("/{id}")
def delete_licencia_software(id: int, db_session: Session = Depends(db.get_db)):
    deleted = crud.delete_licencia_software(db_session, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Licencia no encontrada")
    return {"message": "Licencia eliminada correctamente"}
