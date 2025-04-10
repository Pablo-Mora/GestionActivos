from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

# ---------- Empleados ----------
class Empleado(Base):
    __tablename__ = "empleados"

    Id = Column(Integer, primary_key=True, index=True)
    Fecha = Column(Date)
    ClaseActa = Column(String)
    Nombre = Column(String)
    Identificacion = Column(String, unique=True, index=True)
    Cargo = Column(String)
    Dependencia = Column(String)
    UbicacionOficina = Column(String)

    activos_hardware = relationship("ActivoHardware", back_populates="empleado", cascade="all, delete-orphan")
    licencias_software = relationship("LicenciaSoftware", back_populates="empleado", cascade="all, delete-orphan")
    accesos_web = relationship("AccesoWeb", back_populates="empleado", cascade="all, delete-orphan")
    responsables_entrega = relationship("ResponsableEntrega", back_populates="empleado", cascade="all, delete-orphan")
    aprobaciones = relationship("Aprobacion", back_populates="empleado", cascade="all, delete-orphan")

# ---------- Activos Hardware ----------
class ActivoHardware(Base):
    __tablename__ = "activos_hardware"

    Id = Column(Integer, primary_key=True, index=True)
    EmpleadoId = Column(Integer, ForeignKey("empleados.Id"))
    TipoHardware = Column(String)
    Cantidad = Column(Integer)
    Marca = Column(String)
    Modelo = Column(String)
    Serial = Column(String)
    Observaciones = Column(String)

    empleado = relationship("Empleado", back_populates="activos_hardware")

# ---------- Licencias Software ----------
class LicenciaSoftware(Base):
    __tablename__ = "licencias_software"

    Id = Column(Integer, primary_key=True, index=True)
    EmpleadoId = Column(Integer, ForeignKey("empleados.Id"))
    NombreLicencia = Column(String)
    Usuario = Column(String)
    Contrasena = Column(String)
    ObligadoCambio = Column(Boolean)

    empleado = relationship("Empleado", back_populates="licencias_software")

# ---------- Accesos Web ----------
class AccesoWeb(Base):
    __tablename__ = "accesos_web"

    Id = Column(Integer, primary_key=True, index=True)
    EmpleadoId = Column(Integer, ForeignKey("empleados.Id"))
    URL = Column(String)
    Usuario = Column(String)
    Contrasena = Column(String)
    ObligadoCambio = Column(Boolean)

    empleado = relationship("Empleado", back_populates="accesos_web")

# ---------- Responsables Entrega ----------
class ResponsableEntrega(Base):
    __tablename__ = "responsables_entrega"

    Id = Column(Integer, primary_key=True, index=True)
    EmpleadoId = Column(Integer, ForeignKey("empleados.Id"))
    Recibe = Column(String)
    Entrega = Column(String)
    RolRecibe = Column(String)
    RolEntrega = Column(String)

    empleado = relationship("Empleado", back_populates="responsables_entrega")

# ---------- Aprobaciones ----------
class Aprobacion(Base):
    __tablename__ = "aprobaciones"

    Id = Column(Integer, primary_key=True, index=True)
    EmpleadoId = Column(Integer, ForeignKey("empleados.Id"))
    AprobadoPor = Column(String)
    CargoAprobador = Column(String)

    empleado = relationship("Empleado", back_populates="aprobaciones")
