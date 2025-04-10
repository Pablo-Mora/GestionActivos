from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.crud.generar_acta import get_empleado_con_todo, generar_documento_word
from fastapi.responses import FileResponse
import os

router = APIRouter(prefix="/acta", tags=["Generar Acta"])

@router.get("/{identificacion}/generar", response_class=FileResponse)
def generar_acta(identificacion: str, db: Session = Depends(get_db)):
    empleado = get_empleado_con_todo(db, identificacion)

    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    ruta_documento = generar_documento_word(empleado)

    if not os.path.exists(ruta_documento):
        raise HTTPException(status_code=500, detail="Error al generar el acta")

    return FileResponse(
        path=ruta_documento,
        filename=os.path.basename(ruta_documento),
        media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
