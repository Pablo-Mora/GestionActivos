from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas.schemas import AprobacionOut, AprobacionCreate, AprobacionUpdate
from app.crud import aprobaciones

router = APIRouter(prefix="/aprobaciones", tags=["Aprobaciones"])

@router.get("/", response_model=list[AprobacionOut])
def get_all(db: Session = Depends(get_db)):
    return aprobaciones.get_all(db)

@router.post("/", response_model=AprobacionOut)
def create(data: AprobacionCreate, db: Session = Depends(get_db)):
    return aprobaciones.create(db, data)

@router.put("/{id}", response_model=AprobacionOut)
def update(id: int, data: AprobacionUpdate, db: Session = Depends(get_db)):
    return aprobaciones.update(db, id, data)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return aprobaciones.delete(db, id)
