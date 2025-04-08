from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Backend.app.Db import db
from Backend.app.schemas.schemas import ResponsableEntregaCreate, ResponsableEntregaUpdate
from app import crud

router = APIRouter(
    prefix="/responsables_entrega",
    tags=["Responsables de Entrega"]
)

@router.get("/")
def get_responsables_entrega(db_session: Session = Depends(db.get_db)):
    return crud.get_responsables_entrega(db_session)

@router.get("/{id}")
def get_responsable_entrega_by_id(id: int, db_session: Session = Depends(db.get_db)):
    responsable = crud.get_responsable_entrega_by_id(db_session, id)
    if not responsable:
        raise HTTPException(status_code=404, detail="Responsable no encontrado")
    return responsable

@router.post("/")
def create_responsable_entrega(responsable: ResponsableEntregaCreate, db_session: Session = Depends(db.get_db)):
    return crud.create_responsable_entrega(db_session, responsable)

@router.put("/{id}")
def update_responsable_entrega(id: int, responsable: ResponsableEntregaUpdate, db_session: Session = Depends(db.get_db)):
    updated = crud.update_responsable_entrega(db_session, id, responsable)
    if not updated:
        raise HTTPException(status_code=404, detail="Responsable no encontrado")
    return {"message": "Responsable actualizado correctamente"}

@router.delete("/{id}")
def delete_responsable_entrega(id: int, db_session: Session = Depends(db.get_db)):
    deleted = crud.delete_responsable_entrega(db_session, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Responsable no encontrado")
    return {"message": "Responsable eliminado correctamente"}