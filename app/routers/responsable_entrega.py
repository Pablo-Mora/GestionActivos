from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.db import get_db
from app.schemas import ResponsableEntregaCreate, ResponsableEntregaUpdate, ResponsableEntregaOut
from app.crud import responsable_entrega

router = APIRouter(prefix="/responsables", tags=["Responsables Entrega"])

@router.get("/", response_model=List[ResponsableEntregaOut])
def get_all_responsables(
    empleado_id: Optional[int] = Query(None),
    recibe: Optional[str] = Query(None),
    entrega: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    return responsable_entrega.get_filtered(db, empleado_id=empleado_id, recibe=recibe, entrega=entrega)

@router.get("/{id}", response_model=ResponsableEntregaOut)
def get_responsable(id: int, db: Session = Depends(get_db)):
    responsable = responsable_entrega.get_by_id(db, id)
    if not responsable:
        raise HTTPException(status_code=404, detail="Responsable de entrega no encontrado")
    return responsable

@router.post("/", response_model=ResponsableEntregaOut)
def create_responsable(data: ResponsableEntregaCreate, db: Session = Depends(get_db)):
    return responsable_entrega.create(db, data)

@router.put("/{id}", response_model=ResponsableEntregaOut)
def update_responsable(id: int, data: ResponsableEntregaUpdate, db: Session = Depends(get_db)):
    updated = responsable_entrega.update(db, id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Responsable de entrega no encontrado")
    return updated

@router.delete("/{id}")
def delete_responsable(id: int, db: Session = Depends(get_db)):
    deleted = responsable_entrega.delete(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Responsable de entrega no encontrado")
    return {"message": "Responsable de entrega eliminado correctamente"}
