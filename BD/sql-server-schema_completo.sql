
-- ========================
-- ESQUEMA BASE DE DATOS: GESTIÓN DE ACTIVOS TIC
-- ========================

-- Tabla de empleados
CREATE TABLE Empleados (
    IdEmpleado INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) NOT NULL,
    Identificacion NVARCHAR(20) NOT NULL UNIQUE,
    Cargo NVARCHAR(100),
    Dependencia NVARCHAR(100),
    UbicacionOficina NVARCHAR(100)
);

-- Tabla de actas
CREATE TABLE Actas (
    IdActa INT PRIMARY KEY IDENTITY(1,1),
    Fecha DATE NOT NULL,
    ClaseActa NVARCHAR(100),
    Version NVARCHAR(10),
    Codigo NVARCHAR(20),
    IdEmpleado INT FOREIGN KEY REFERENCES Empleados(IdEmpleado),
    Observaciones NVARCHAR(MAX),
    FirmadoPorEmpleado BIT DEFAULT 0,
    FirmadoPorEntregador BIT DEFAULT 0,
    FirmadoPorAprobador BIT DEFAULT 0
);

-- Tabla de hardware entregado
CREATE TABLE HardwareEntregado (
    IdHardware INT PRIMARY KEY IDENTITY(1,1),
    IdActa INT FOREIGN KEY REFERENCES Actas(IdActa),
    TipoHardware NVARCHAR(100),
    Cantidad INT,
    Marca NVARCHAR(100),
    Modelo NVARCHAR(100),
    Serial NVARCHAR(100),
    Observaciones NVARCHAR(MAX)
);

-- Tabla de software y licencias entregadas
CREATE TABLE SoftwareLicencias (
    IdLicencia INT PRIMARY KEY IDENTITY(1,1),
    IdActa INT FOREIGN KEY REFERENCES Actas(IdActa),
    TipoLicencia NVARCHAR(100),
    Usuario NVARCHAR(100),
    Contrasena NVARCHAR(100),
    ObligadoCambio BIT DEFAULT 1
);

-- Tabla de credenciales especiales entregadas
CREATE TABLE CredencialesEspeciales (
    IdCredencial INT PRIMARY KEY IDENTITY(1,1),
    IdActa INT FOREIGN KEY REFERENCES Actas(IdActa),
    URL NVARCHAR(200),
    Usuario NVARCHAR(100),
    Contrasena NVARCHAR(100),
    ObligadoCambio BIT DEFAULT 1
);

-- Tabla de firmas responsables
CREATE TABLE Firmas (
    IdFirma INT PRIMARY KEY IDENTITY(1,1),
    IdActa INT FOREIGN KEY REFERENCES Actas(IdActa),
    TipoFirma NVARCHAR(50),
    NombreFirmante NVARCHAR(100),
    CargoFirmante NVARCHAR(100),
    FechaFirma DATETIME DEFAULT GETDATE()
);

-- Tabla opcional para registro de aceptación de acuerdos
CREATE TABLE AceptacionLegal (
    IdAceptacion INT PRIMARY KEY IDENTITY(1,1),
    IdActa INT FOREIGN KEY REFERENCES Actas(IdActa),
    AceptaAcuerdos BIT DEFAULT 1,
    AceptaCompromisos BIT DEFAULT 1,
    AceptaRecomendaciones BIT DEFAULT 1,
    FechaAceptacion DATETIME DEFAULT GETDATE()
);
