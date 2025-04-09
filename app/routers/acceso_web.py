from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas import AccesoWebCreate, AccesoWebUpdate, AccesoWebOut
from app.crud import acceso_web

router = APIRouter(prefix="/accesos-web", tags=["Accesos Web"])

@router.get("/", response_model=list[AccesoWebOut])
def get_all(db: Session = Depends(get_db)):
    return acceso_web.get_all(db)

@router.post("/", response_model=AccesoWebOut)
def create(data: AccesoWebCreate, db: Session = Depends(get_db)):
    return acceso_web.create(db, data)

@router.put("/{id}", response_model=AccesoWebOut)
def update(id: int, data: AccesoWebUpdate, db: Session = Depends(get_db)):
    updated = acceso_web.update(db, id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Acceso web no encontrado")
    return updated

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    deleted = acceso_web.delete(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Acceso web no encontrado")
    return {"message": "Acceso web eliminado correctamente"}
