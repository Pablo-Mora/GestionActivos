from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import (
    empleados, 
    activos_hardware, 
    licencias_software, 
    acceso_web, 
    responsable_entrega, 
    aprobaciones, 
    acta
)

app = FastAPI(title="API Gestión de Activos TIC")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes cambiar esto por dominios específicos en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(empleados.router, prefix="/empleados", tags=["Empleados"])
app.include_router(activos_hardware.router, prefix="/hardware", tags=["Activos Hardware"])
app.include_router(licencias_software.router, prefix="/licencias", tags=["Licencias Software"])
app.include_router(acceso_web.router, prefix="/accesos", tags=["Accesos Web"])
app.include_router(responsable_entrega.router, prefix="/responsables", tags=["Responsables Entrega"])
app.include_router(aprobaciones.router, prefix="/aprobaciones", tags=["Aprobaciones"])
app.include_router(acta.router)

# Ruta raíz
@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)
