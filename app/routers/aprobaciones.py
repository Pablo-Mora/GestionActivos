from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas import AprobacionCreate, AprobacionUpdate, AprobacionOut
from app.crud import aprobaciones

router = APIRouter(prefix="/aprobaciones", tags=["Aprobaciones"])

# Obtener todos con filtros dinámicos
@router.get("/", response_model=list[AprobacionOut])
def get_all(
    empleado_id: int = Query(None),
    aprobado_por: str = Query(None),
    db: Session = Depends(get_db)
):
    return aprobaciones.get_filtered(db, empleado_id, aprobado_por)

# Obtener por ID
@router.get("/{id}", response_model=AprobacionOut)
def get_by_id(id: int, db: Session = Depends(get_db)):
    item = aprobaciones.get_by_id(db, id)
    if not item:
        raise HTTPException(status_code=404, detail="Aprobación no encontrada")
    return item

# Crear
@router.post("/", response_model=AprobacionOut)
def create(data: AprobacionCreate, db: Session = Depends(get_db)):
    return aprobaciones.create(db, data)

# Actualizar
@router.put("/{id}", response_model=AprobacionOut)
def update(id: int, data: AprobacionUpdate, db: Session = Depends(get_db)):
    item = aprobaciones.update(db, id, data)
    if not item:
        raise HTTPException(status_code=404, detail="Aprobación no encontrada")
    return item

# Eliminar
@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    deleted = aprobaciones.delete(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Aprobación no encontrada")
    return {"message": "Aprobación eliminada correctamente"}
