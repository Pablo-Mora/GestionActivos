from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# ---------- Empleados ----------
class EmpleadoBase(BaseModel):
    Fecha: date
    ClaseActa: str
    Nombre: str
    Identificacion: str
    Cargo: str
    Dependencia: str
    UbicacionOficina: str

class EmpleadoCreate(EmpleadoBase):
    pass

class Empleado(EmpleadoBase):
    Id: int
    class Config:
        orm_mode = True

# ---------- ActivosHardware ----------
class ActivoHardwareBase(BaseModel):
    EmpleadoId: int
    TipoHardware: str
    Cantidad: int
    Marca: str
    Modelo: str
    Serial: str
    Observaciones: Optional[str] = None

class ActivoHardwareCreate(ActivoHardwareBase):
    pass

class ActivoHardware(ActivoHardwareBase):
    Id: int
    class Config:
        orm_mode = True

# ---------- LicenciasSoftware ----------
class LicenciaSoftwareBase(BaseModel):
    EmpleadoId: int
    NombreLicencia: str
    Usuario: str
    Contrasena: str
    ObligadoCambio: bool

class LicenciaSoftwareCreate(LicenciaSoftwareBase):
    pass

class LicenciaSoftware(LicenciaSoftwareBase):
    Id: int
    class Config:
        orm_mode = True

# ---------- AccesosWeb ----------
class AccesoWebBase(BaseModel):
    EmpleadoId: int
    URL: str
    Usuario: str
    Contrasena: str
    ObligadoCambio: bool

class AccesoWebCreate(AccesoWebBase):
    pass

class AccesoWeb(AccesoWebBase):
    Id: int
    class Config:
        orm_mode = True

# ---------- ResponsablesEntrega ----------
class ResponsableEntregaBase(BaseModel):
    EmpleadoId: int
    Recibe: str
    Entrega: str
    RolRecibe: str
    RolEntrega: str

class ResponsableEntregaCreate(ResponsableEntregaBase):
    pass

class ResponsableEntrega(ResponsableEntregaBase):
    Id: int
    class Config:
        orm_mode = True

# ---------- Aprobaciones ----------
class AprobacionBase(BaseModel):
    EmpleadoId: int
    AprobadoPor: str
    CargoAprobador: str

class AprobacionCreate(AprobacionBase):
    pass

class Aprobacion(AprobacionBase):
    Id: int
    class Config:
        orm_mode = True
