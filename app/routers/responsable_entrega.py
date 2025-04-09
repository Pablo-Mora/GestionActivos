from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas import ResponsableEntregaCreate, ResponsableEntregaUpdate, ResponsableEntregaOut
from app.crud import responsable_entrega

router = APIRouter(prefix="/responsables", tags=["Responsables Entrega"])

@router.get("/", response_model=list[ResponsableEntregaOut])
def get_all(db: Session = Depends(get_db)):
    return responsable_entrega.get_all(db)

@router.post("/", response_model=ResponsableEntregaOut)
def create(data: ResponsableEntregaCreate, db: Session = Depends(get_db)):
    return responsable_entrega.create(db, data)

@router.put("/{id}", response_model=ResponsableEntregaOut)
def update(id: int, data: ResponsableEntregaUpdate, db: Session = Depends(get_db)):
    updated = responsable_entrega.update(db, id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Responsable no encontrado")
    return updated

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    deleted = responsable_entrega.delete(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Responsable no encontrado")
    return {"message": "Responsable eliminado correctamente"}
