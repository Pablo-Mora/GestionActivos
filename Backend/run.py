from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    empleados,
    activos_hardware,
    licencias_software,
    accesos_web,
    responsables_entrega,
    aprobaciones
)

app = FastAPI(title="API Gestión de Activos TIC")

# CORS (opcional si accedes desde un frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar los routers
app.include_router(empleados.router, prefix="/empleados", tags=["Empleados"])
app.include_router(activos_hardware.router, prefix="/hardware", tags=["Activos Hardware"])
app.include_router(licencias_software.router, prefix="/licencias", tags=["Licencias Software"])
app.include_router(accesos_web.router, prefix="/accesos", tags=["Accesos Web"])
app.include_router(responsables_entrega.router, prefix="/responsables", tags=["Responsables Entrega"])
app.include_router(aprobaciones.router, prefix="/aprobaciones", tags=["Aprobaciones"])
