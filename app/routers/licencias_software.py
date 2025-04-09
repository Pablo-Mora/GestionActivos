from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas import LicenciaSoftwareCreate, LicenciaSoftwareUpdate, LicenciaSoftwareOut
from app.crud import licencias_software

router = APIRouter(prefix="/licencias", tags=["Licencias Software"])

@router.get("/", response_model=list[LicenciaSoftwareOut])
def get_all(db: Session = Depends(get_db)):
    return licencias_software.get_all(db)

@router.post("/", response_model=LicenciaSoftwareOut)
def create(data: LicenciaSoftwareCreate, db: Session = Depends(get_db)):
    return licencias_software.create(db, data)

@router.put("/{id}", response_model=LicenciaSoftwareOut)
def update(id: int, data: LicenciaSoftwareUpdate, db: Session = Depends(get_db)):
    updated = licencias_software.update(db, id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Licencia no encontrada")
    return updated

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    deleted = licencias_software.delete(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Licencia no encontrada")
    return {"message": "Licencia eliminada correctamente"}
