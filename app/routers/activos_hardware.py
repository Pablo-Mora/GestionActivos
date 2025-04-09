from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas.schemas import ActivoHardwareOut, ActivoHardwareCreate, ActivoHardwareUpdate
from app.crud import activos_hardware

router = APIRouter(prefix="/hardware", tags=["ActivosHardware"])

@router.get("/", response_model=list[ActivoHardwareOut])
def get_all(db: Session = Depends(get_db)):
    return activos_hardware.get_all(db)

@router.post("/", response_model=ActivoHardwareOut)
def create(data: ActivoHardwareCreate, db: Session = Depends(get_db)):
    return activos_hardware.create(db, data)

@router.put("/{id}", response_model=ActivoHardwareOut)
def update(id: int, data: ActivoHardwareUpdate, db: Session = Depends(get_db)):
    return activos_hardware.update(db, id, data)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return activos_hardware.delete(db, id)
