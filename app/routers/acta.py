from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.crud.generar_acta import get_empleado_con_todo
from docxtpl import DocxTemplate
import os

router = APIRouter(prefix="/acta", tags=["Actas"])

@router.get("/generar/{empleado_id}")
def generar_acta(empleado_id: int, db: Session = Depends(get_db)):
    datos = get_empleado_con_todo(db, empleado_id)
    if not datos:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    doc = DocxTemplate("templates/plantilla_acta.docx")
    context = {
        "HARDWARE": datos["hardware_items"],
        "LICENCIAS": datos["licencias_items"],
        "NOMBRE": datos["empleado"].Nombre,
        "CARGO": datos["empleado"].Cargo,
        "FECHA": str(datos["empleado"].Fecha),
        "IDENTIFICACION": datos["empleado"].Identificacion,
        "DEPENDENCIA": datos["empleado"].Dependencia,
        "UBICACION": datos["empleado"].UbicacionOficina,
    }

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    filename = f"acta_{datos['empleado'].Nombre.replace(' ', '_')}.docx"
    filepath = os.path.join(output_dir, filename)

    doc.render(context)
    doc.save(filepath)

    return {"archivo": filename, "ruta": filepath}
