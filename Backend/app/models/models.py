from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Empleado(Base):
    __tablename__ = 'Empleados'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Fecha = Column(Date)
    ClaseActa = Column(String(100))
    Nombre = Column(String(100))
    Identificacion = Column(String(50))
    Cargo = Column(String(100))
    Dependencia = Column(String(100))
    UbicacionOficina = Column(String(100))

    activos_hardware = relationship("ActivoHardware", back_populates="empleado")
    licencias_software = relationship("LicenciaSoftware", back_populates="empleado")
    accesos_web = relationship("AccesoWeb", back_populates="empleado")
    responsables_entrega = relationship("ResponsableEntrega", back_populates="empleado")
    aprobaciones = relationship("Aprobacion", back_populates="empleado")


class ActivoHardware(Base):
    __tablename__ = 'ActivosHardware'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    EmpleadoId = Column(Integer, ForeignKey('Empleados.Id'))
    TipoHardware = Column(String(100))
    Cantidad = Column(Integer)
    Marca = Column(String(100))
    Modelo = Column(String(100))
    Serial = Column(String(100))
    Observaciones = Column(String(255))

    empleado = relationship("Empleado", back_populates="activos_hardware")


class LicenciaSoftware(Base):
    __tablename__ = 'LicenciasSoftware'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    EmpleadoId = Column(Integer, ForeignKey('Empleados.Id'))
    NombreLicencia = Column(String(100))
    Usuario = Column(String(100))
    Contrasena = Column(String(100))
    ObligadoCambio = Column(Boolean)

    empleado = relationship("Empleado", back_populates="licencias_software")


class AccesoWeb(Base):
    __tablename__ = 'AccesosWeb'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    EmpleadoId = Column(Integer, ForeignKey('Empleados.Id'))
    URL = Column(String(255))
    Usuario = Column(String(100))
    Contrasena = Column(String(100))
    ObligadoCambio = Column(Boolean)

    empleado = relationship("Empleado", back_populates="accesos_web")


class ResponsableEntrega(Base):
    __tablename__ = 'ResponsablesEntrega'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    EmpleadoId = Column(Integer, ForeignKey('Empleados.Id'))
    Recibe = Column(String(100))
    Entrega = Column(String(100))
    RolRecibe = Column(String(100))
    RolEntrega = Column(String(100))

    empleado = relationship("Empleado", back_populates="responsables_entrega")


class Aprobacion(Base):
    __tablename__ = 'Aprobaciones'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    EmpleadoId = Column(Integer, ForeignKey('Empleados.Id'))
    AprobadoPor = Column(String(100))
    CargoAprobador = Column(String(100))

    empleado = relationship("Empleado", back_populates="aprobaciones")