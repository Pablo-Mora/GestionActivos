import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';
import './EmployeeDetails.css';

const API_URL = 'http://localhost:5000/api';

function EmployeeDetails() {
    const { id } = useParams();
    const [employee, setEmployee] = useState(null);
    const [assets, setAssets] = useState([]);
    const [software, setSoftware] = useState([]);
    const [credentials, setCredentials] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [activeTab, setActiveTab] = useState('info');

    useEffect(() => {
        fetchEmployeeData();
    }, [id]);

    const fetchEmployeeData = async () => {
        try {
        setLoading(true);
        
        // Fetch employee details
        const employeeResponse = await axios.get(`${API_URL}/employees/${id}`);
        setEmployee(employeeResponse.data);
        
        // Fetch employee assets
        const assetsResponse = await axios.get(`${API_URL}/employees/${id}/assets`);
        setAssets(assetsResponse.data);
        
        // Fetch employee software
        const softwareResponse = await axios.get(`${API_URL}/employees/${id}/software`);
        setSoftware(softwareResponse.data);
        
        // Fetch employee credentials
        const credentialsResponse = await axios.get(`${API_URL}/employees/${id}/credentials`);
        setCredentials(credentialsResponse.data);
        
        setLoading(false);
        } catch (err) {
        setError('Error al cargar la información del empleado.');
        setLoading(false);
        console.error('Error fetching employee data:', err);
        }
    };

    const handleExportExcel = () => {
        window.open(`${API_URL}/export/excel/${id}`, '_blank');
    };

    const handleExportWord = () => {
        window.open(`${API_URL}/export/word/${id}`, '_blank');
    };

    if (loading) {
        return <div className="loading">Cargando información del empleado...</div>;
    }

    if (error) {
        return <div className="error-message">{error}</div>;
    }

    if (!employee) {
        return <div className="error-message">No se encontró información del empleado.</div>;
    }

    return (
        <div className="employee-details-container">
        <div className="employee-header">
            <h2>Detalles del Empleado</h2>
            <div className="action-buttons">
            <Link to="/employees" className="button secondary">Volver a la Lista</Link>
            <button onClick={handleExportExcel} className="button primary">Exportar a Excel</button>
            <button onClick={handleExportWord} className="button primary">Generar Acta</button>
            </div>
        </div>
        
        <div className="employee-info-card">
            <div className="info-row">
            <div className="info-item">
                <span className="label">Identificación:</span>
                <span className="value">{employee.identificationNumber}</span>
            </div>
            <div className="info-item">
                <span className="label">Nombre Completo:</span>
                <span className="value">{employee.fullName}</span>
            </div>
            </div>
            <div className="info-row">
            <div className="info-item">
                <span className="label">Cargo:</span>
                <span className="value">{employee.position}</span>
            </div>
            <div className="info-item">
                <span className="label">Departamento:</span>
                <span className="value">{employee.department}</span>
            </div>
            </div>
            <div className="info-row">
            <div className="info-item">
                <span className="label">Ubicación:</span>
                <span className="value">{employee.officeLocation || 'No especificada'}</span>
            </div>
            </div>
        </div>
        
        <div className="tabs-container">
            <div className="tabs-header">
            <button 
                className={`tab-button ${activeTab === 'info' ? 'active' : ''}`}
                onClick={() => setActiveTab('info')}
            >
                Información General
            </button>
            <button 
                className={`tab-button ${activeTab === 'assets' ? 'active' : ''}`}
                onClick={() => setActiveTab('assets')}
            >
                Activos ({assets.length})
            </button>
            <button 
                className={`tab-button ${activeTab === 'software' ? 'active' : ''}`}
                onClick={() => setActiveTab('software')}
            >
                Software ({software.length})
            </button>
            <button 
                className={`tab-button ${activeTab === 'credentials' ? 'active' : ''}`}
                onClick={() => setActiveTab('credentials')}
            >
                Credenciales ({credentials.length})
            </button>
            </div>
            
            <div className="tab-content">
            {activeTab === 'info' && (
                <div className="info-tab">
                <p>El empleado <strong>{employee.fullName}</strong> trabaja como <strong>{employee.position}</strong> en el departamento de <strong>{employee.department}</strong>.</p>
                {employee.officeLocation && <p>Ubicación de oficina: <strong>{employee.officeLocation}</strong></p>}
                </div>
            )}
            
            {activeTab === 'assets' && (
                <div className="assets-tab">
                {assets.length > 0 ? (
                    <div className="table-container">
                    <table className="data-table">
                        <thead>
                        <tr>
                            <th>Categoría</th>
                            <th>Marca</th>
                            <th>Modelo</th>
                            <th>Número de Serie</th>
                            <th>Fecha de Asignación</th>
                            <th>Observaciones</th>
                        </tr>
                        </thead>
                        <tbody>
                        {assets.map((asset, index) => (
                            <tr key={index}>
                            <td>{asset.category}</td>
                            <td>{asset.brand}</td>
                            <td>{asset.model}</td>
                            <td>{asset.serialNumber}</td>
                            <td>{asset.assignmentDate}</td>
                            <td>{asset.observations}</td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                    </div>
                ) : (
                    <p className="no-data">No hay activos asignados a este empleado.</p>
                )}
                </div>
            )}
            
            {activeTab === 'software' && (
                <div className="software-tab">
                {software.length > 0 ? (
                    <div className="table-container">
                    <table className="data-table">
                        <thead>
                        <tr>
                            <th>Licencia</th>
                            <th>Usuario</th>
                            <th>Requiere Cambio de Contraseña</th>
                        </tr>
                        </thead>
                        <tbody>
                        {software.map((sw, index) => (
                            <tr key={index}>
                            <td>{sw.licenseName}</td>
                            <td>{sw.username}</td>
                            <td>{sw.requiresPasswordChange ? 'Sí' : 'No'}</td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                    </div>
                ) : (
                    <p className="no-data">No hay licencias de software asignadas a este empleado.</p>
                )}
                </div>
            )}
            
            {activeTab === 'credentials' && (
                <div className="credentials-tab">
                {credentials.length > 0 ? (
                    <div className="table-container">
                    <table className="data-table">
                        <thead>
                        <tr>
                            <th>URL</th>
                            <th>Usuario</th>
                            <th>Requiere Cambio de Contraseña</th>
                        </tr>
                        </thead>
                        <tbody>
                        {credentials.map((cred, index) => (
                            <tr key={index}>
                            <td>{cred.url}</td>
                            <td>{cred.username}</td>
                            <td>{cred.requiresPasswordChange ? 'Sí' : 'No'}</td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                    </div>
                ) : (
                    <p className="no-data">No hay credenciales especiales asignadas a este empleado.</p>
                )}
                </div>
            )}
            </div>
        </div>
        </div>
    );
    }

export default EmployeeDetails;