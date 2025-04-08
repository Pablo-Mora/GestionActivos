from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Backend.app.Db import db
from Backend.app.schemas.schemas import AccesoWebCreate, AccesoWebUpdate
from app import crud

router = APIRouter(
    prefix="/accesos_web",
    tags=["Accesos Web"]
)

@router.get("/")
def get_accesos_web(db_session: Session = Depends(db.get_db)):
    return crud.get_accesos_web(db_session)

@router.get("/{id}")
def get_acceso_web_by_id(id: int, db_session: Session = Depends(db.get_db)):
    acceso = crud.get_acceso_web_by_id(db_session, id)
    if not acceso:
        raise HTTPException(status_code=404, detail="Acceso web no encontrado")
    return acceso

@router.post("/")
def create_acceso_web(acceso: AccesoWebCreate, db_session: Session = Depends(db.get_db)):
    return crud.create_acceso_web(db_session, acceso)

@router.put("/{id}")
def update_acceso_web(id: int, acceso: AccesoWebUpdate, db_session: Session = Depends(db.get_db)):
    updated = crud.update_acceso_web(db_session, id, acceso)
    if not updated:
        raise HTTPException(status_code=404, detail="Acceso web no encontrado")
    return {"message": "Acceso web actualizado correctamente"}

@router.delete("/{id}")
def delete_acceso_web(id: int, db_session: Session = Depends(db.get_db)):
    deleted = crud.delete_acceso_web(db_session, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Acceso web no encontrado")
    return {"message": "Acceso web eliminado correctamente"}