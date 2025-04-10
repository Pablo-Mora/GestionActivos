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

class EmpleadoUpdate(BaseModel):
    Fecha: date
    ClaseActa: str
    Nombre: str
    Identificacion: str
    Cargo: str
    Dependencia: str
    UbicacionOficina: str

    class Config:
        from_attributes = True

class EmpleadoOut(BaseModel):
    Id: int
    Fecha: date
    ClaseActa: str
    Nombre: str
    Identificacion: str
    Cargo: str
    Dependencia: str
    UbicacionOficina: str

    class Config:
        from_attributes = True

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

class ActivoHardwareUpdate(BaseModel):
    TipoHardware: str
    Cantidad: int
    Marca: str
    Modelo: str
    Serial: str
    Observaciones: Optional[str] = None

    class Config:
        from_attributes = True

class ActivoHardwareOut(BaseModel):
    Id: int
    EmpleadoId: int
    TipoHardware: str
    Cantidad: int
    Marca: str
    Modelo: str
    Serial: str
    Observaciones: Optional[str] = None

    class Config:
        from_attributes = True

# ---------- LicenciasSoftware ----------
class LicenciaSoftwareBase(BaseModel):
    EmpleadoId: int
    NombreLicencia: str
    Usuario: str
    Contrasena: str
    ObligadoCambio: bool

class LicenciaSoftwareCreate(LicenciaSoftwareBase):
    pass

class LicenciaSoftwareUpdate(BaseModel):
    NombreLicencia: str
    Usuario: str
    Contrasena: str
    ObligadoCambio: bool

    class Config:
        from_attributes = True

class LicenciaSoftwareOut(BaseModel):
    Id: int
    EmpleadoId: int
    NombreLicencia: str
    Usuario: str
    Contrasena: str
    ObligadoCambio: bool

    class Config:
        from_attributes = True

# ---------- AccesosWeb ----------
class AccesoWebBase(BaseModel):
    EmpleadoId: int
    URL: str
    Usuario: str
    Contrasena: str
    ObligadoCambio: bool

class AccesoWebCreate(AccesoWebBase):
    pass

class AccesoWebUpdate(BaseModel):
    URL: str
    Usuario: str
    Contrasena: str
    ObligadoCambio: bool

    class Config:
        from_attributes = True

class AccesoWebOut(BaseModel):
    Id: int
    EmpleadoId: int
    URL: str
    Usuario: str
    Contrasena: str
    ObligadoCambio: bool

    class Config:
        from_attributes = True

# ---------- ResponsablesEntrega ----------
class ResponsableEntregaBase(BaseModel):
    EmpleadoId: int
    Recibe: str
    Entrega: str
    RolRecibe: str
    RolEntrega: str

class ResponsableEntregaCreate(ResponsableEntregaBase):
    pass

class ResponsableEntregaUpdate(BaseModel):
    Recibe: str
    Entrega: str
    RolRecibe: str
    RolEntrega: str

    class Config:
        from_attributes = True

class ResponsableEntregaOut(BaseModel):
    Id: int
    EmpleadoId: int
    Recibe: str
    Entrega: str
    RolRecibe: str
    RolEntrega: str

    class Config:
        from_attributes = True

# ---------- Aprobaciones ----------
class AprobacionBase(BaseModel):
    EmpleadoId: int
    AprobadoPor: str
    CargoAprobador: str

class AprobacionCreate(AprobacionBase):
    pass

class AprobacionUpdate(BaseModel):
    AprobadoPor: str
    CargoAprobador: str

    class Config:
        from_attributes = True

class AprobacionOut(BaseModel):
    Id: int
    EmpleadoId: int
    AprobadoPor: str
    CargoAprobador: str

    class Config:
        from_attributes = True

# ---------- Empleado Detallado ----------
class EmpleadoDetalleOut(BaseModel):
    Id: int
    Fecha: date
    ClaseActa: str
    Nombre: str
    Identificacion: str
    Cargo: str
    Dependencia: str
    UbicacionOficina: str

    activos_hardware: List[ActivoHardwareOut] = []
    licencias_software: List[LicenciaSoftwareOut] = []
    accesos_web: List[AccesoWebOut] = []
    responsables_entrega: List[ResponsableEntregaOut] = []
    aprobaciones: List[AprobacionOut] = []

    class Config:
        from_attributes = True
