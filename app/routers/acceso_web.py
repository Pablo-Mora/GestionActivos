from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.db import get_db
from app.schemas import AccesoWebCreate, AccesoWebUpdate, AccesoWebOut
from app.crud import acceso_web

router = APIRouter(prefix="/accesos", tags=["Accesos Web"])

@router.get("/", response_model=List[AccesoWebOut])
def get_all_accesos(
    empleado_id: Optional[int] = Query(None),
    url: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    return acceso_web.get_filtered(db, empleado_id=empleado_id, url=url)

@router.get("/{id}", response_model=AccesoWebOut)
def get_acceso(id: int, db: Session = Depends(get_db)):
    acceso = acceso_web.get_by_id(db, id)
    if not acceso:
        raise HTTPException(status_code=404, detail="Acceso web no encontrado")
    return acceso

@router.post("/", response_model=AccesoWebOut)
def create_acceso(data: AccesoWebCreate, db: Session = Depends(get_db)):
    return acceso_web.create(db, data)

@router.put("/{id}", response_model=AccesoWebOut)
def update_acceso(id: int, data: AccesoWebUpdate, db: Session = Depends(get_db)):
    updated = acceso_web.update(db, id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Acceso web no encontrado")
    return updated

@router.delete("/{id}")
def delete_acceso(id: int, db: Session = Depends(get_db)):
    deleted = acceso_web.delete(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Acceso web no encontrado")
    return {"message": "Acceso web eliminado correctamente"}
