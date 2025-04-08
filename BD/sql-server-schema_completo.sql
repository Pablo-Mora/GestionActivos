CREATE DATABASE GestionActivos
GO

USE GestionActivos

-- Tabla de empleados
CREATE TABLE Empleados (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Fecha DATE,
    ClaseActa NVARCHAR(100),
    Nombre NVARCHAR(100),
    Identificacion NVARCHAR(50),
    Cargo NVARCHAR(100),
    Dependencia NVARCHAR(100),
    UbicacionOficina NVARCHAR(100)
);

-- Tabla de hardware asignado
CREATE TABLE ActivosHardware (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EmpleadoId INT FOREIGN KEY REFERENCES Empleados(Id),
    TipoHardware NVARCHAR(100),
    Cantidad INT,
    Marca NVARCHAR(100),
    Modelo NVARCHAR(100),
    Serial NVARCHAR(100),
    Observaciones NVARCHAR(255)
);

-- Tabla de licencias de software
CREATE TABLE LicenciasSoftware (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EmpleadoId INT FOREIGN KEY REFERENCES Empleados(Id),
    NombreLicencia NVARCHAR(100),
    Usuario NVARCHAR(100),
    Contrasena NVARCHAR(100),
    ObligadoCambio BIT
);

-- Tabla de accesos web
CREATE TABLE AccesosWeb (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EmpleadoId INT FOREIGN KEY REFERENCES Empleados(Id),
    URL NVARCHAR(255),
    Usuario NVARCHAR(100),
    Contrasena NVARCHAR(100),
    ObligadoCambio BIT
);

-- Tabla de responsables de entrega
CREATE TABLE ResponsablesEntrega (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EmpleadoId INT FOREIGN KEY REFERENCES Empleados(Id),
    Recibe NVARCHAR(100),
    Entrega NVARCHAR(100),
    RolRecibe NVARCHAR(100),
    RolEntrega NVARCHAR(100)
);

-- Tabla de aprobación
CREATE TABLE Aprobaciones (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EmpleadoId INT FOREIGN KEY REFERENCES Empleados(Id),
    AprobadoPor NVARCHAR(100),
    CargoAprobador NVARCHAR(100)
);
