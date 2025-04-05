-- Create database
CREATE DATABASE AssetsManagement;
GO

USE AssetsManagement;
GO

-- Create table for departments
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY IDENTITY(1,1),
    DepartmentName NVARCHAR(100) NOT NULL
);

-- Create table for employees
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY IDENTITY(1,1),
    IdentificationNumber NVARCHAR(20) NOT NULL UNIQUE,
    FullName NVARCHAR(100) NOT NULL,
    Position NVARCHAR(100) NOT NULL,
    DepartmentID INT NOT NULL,
    OfficeLocation NVARCHAR(100),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Create table for asset categories
CREATE TABLE AssetCategories (
    CategoryID INT PRIMARY KEY IDENTITY(1,1),
    CategoryName NVARCHAR(100) NOT NULL UNIQUE
);

-- Create table for brands
CREATE TABLE Brands (
    BrandID INT PRIMARY KEY IDENTITY(1,1),
    BrandName NVARCHAR(100) NOT NULL UNIQUE
);

-- Create table for assets
CREATE TABLE Assets (
    AssetID INT PRIMARY KEY IDENTITY(1,1),
    CategoryID INT NOT NULL,
    BrandID INT NOT NULL,
    Model NVARCHAR(100),
    SerialNumber NVARCHAR(100) UNIQUE,
    Status NVARCHAR(20) NOT NULL DEFAULT 'Available' CHECK (Status IN ('Available', 'Assigned', 'In Repair', 'Retired')),
    FOREIGN KEY (CategoryID) REFERENCES AssetCategories(CategoryID),
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID)
);

-- Create table for software licenses
CREATE TABLE SoftwareLicenses (
    LicenseID INT PRIMARY KEY IDENTITY(1,1),
    LicenseName NVARCHAR(100) NOT NULL,
    LicenseType NVARCHAR(100) NOT NULL,
    RequiresPasswordChange BIT DEFAULT 0
);

-- Create table for asset assignments
CREATE TABLE AssetAssignments (
    AssignmentID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT NOT NULL,
    AssetID INT NOT NULL,
    AssignmentDate DATE NOT NULL,
    ReturnDate DATE NULL,
    Observations NVARCHAR(MAX),
    ActaID INT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (AssetID) REFERENCES Assets(AssetID)
);

-- Create table for software license assignments
CREATE TABLE SoftwareLicenseAssignments (
    SoftwareAssignmentID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT NOT NULL,
    LicenseID INT NOT NULL,
    Username NVARCHAR(100),
    Password NVARCHAR(255),
    AssignmentDate DATE NOT NULL,
    ExpirationDate DATE NULL,
    ActaID INT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (LicenseID) REFERENCES SoftwareLicenses(LicenseID)
);

-- Create table for special credentials
CREATE TABLE SpecialCredentials (
    CredentialID INT PRIMARY KEY IDENTITY(1,1),
    URL NVARCHAR(255) NOT NULL,
    Username NVARCHAR(100) NOT NULL,
    Password NVARCHAR(255) NOT NULL,
    RequiresPasswordChange BIT DEFAULT 0
);

-- Create table for special credential assignments
CREATE TABLE SpecialCredentialAssignments (
    SpecialAssignmentID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT NOT NULL,
    CredentialID INT NOT NULL,
    AssignmentDate DATE NOT NULL,
    ActaID INT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (CredentialID) REFERENCES SpecialCredentials(CredentialID)
);

-- Create table for delivery certificates (Actas)
CREATE TABLE DeliveryCertificates (
    ActaID INT PRIMARY KEY IDENTITY(1,1),
    CertificateType NVARCHAR(100) NOT NULL,
    EmployeeID INT NOT NULL,
    IssueDate DATE NOT NULL,
    ApprovedBy NVARCHAR(100),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Create table for users (system access)
CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) NOT NULL UNIQUE,
    Password NVARCHAR(255) NOT NULL,
    EmployeeID INT NULL,
    Role NVARCHAR(20) NOT NULL DEFAULT 'User' CHECK (Role IN ('Admin', 'Manager', 'User')),
    LastLogin DATETIME NULL,
    IsActive BIT DEFAULT 1,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Insert initial departments
INSERT INTO Departments (DepartmentName) VALUES 
(N'Gerencia General'),
(N'Mercadeo y Ventas'),
(N'Suministros'),
(N'Producción'),
(N'Talento Humano & SG-SST'),
(N'Finanzas y Contabilidad');

-- Insert initial asset categories
INSERT INTO AssetCategories (CategoryName) VALUES 
(N'Celular'),
(N'Cargador de celular'),
(N'Computador de escritorio'),
(N'Computadora portátil'),
(N'Cargador de portátil'),
(N'Monitor'),
(N'Mouse'),
(N'Teclado'),
(N'Teclado numérico'),
(N'Soporte portátil'),
(N'Cable Ethernet'),
(N'Impresora'),
(N'SimCard'),
(N'Sim Virtual');

-- Insert initial software licenses
INSERT INTO SoftwareLicenses (LicenseName, LicenseType, RequiresPasswordChange) VALUES 
(N'Antivirus', N'Security', 1),
(N'Iventas', N'Business', 1),
(N'Microsoft 365', N'Office', 1),
(N'Siesa 8.5', N'Business', 1),
(N'Siesa Acces', N'Business', 1),
(N'Siesa Cloud', N'Business', 1),
(N'Siesa Enterprise', N'Business', 1);

-- Create stored procedure