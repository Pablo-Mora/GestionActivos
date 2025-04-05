import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AssetAssignment.css';

const API_URL = 'http://localhost:5000/api';

function AssetAssignment() {
    const [employees, setEmployees] = useState([]);
    const [assets, setAssets] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [successMessage, setSuccessMessage] = useState('');
    
    // Form state
    const [selectedEmployee, setSelectedEmployee] = useState('');
    const [selectedAsset, setSelectedAsset] = useState('');
    const [observations, setObservations] = useState('');
    const [assignmentDate, setAssignmentDate] = useState(new Date().toISOString().split('T')[0]);

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
        setLoading(true);
        setError(null);
        
        // Fetch employees and available assets in parallel
        const [employeesResponse, assetsResponse] = await Promise.all([
            axios.get(`${API_URL}/employees`),
            axios.get(`${API_URL}/assets`)
        ]);
        
        setEmployees(employeesResponse.data);
        
        // Filter only available assets
        const availableAssets = assetsResponse.data.filter(asset => asset.status === 'Available');
        setAssets(availableAssets);
        
        setLoading(false);
        } catch (err) {
        setError('Error al cargar los datos. Por favor, intente nuevamente.');
        setLoading(false);
        console.error('Error fetching data:', err);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (!selectedEmployee || !selectedAsset) {
        setError('Debe seleccionar un empleado y un activo.');
        return;
        }
        
        try {
        setLoading(true);
        setError(null);
        
        const assignmentData = {
            employeeId: parseInt(selectedEmployee),
            assetId: parseInt(selectedAsset),
            assignmentDate,
            observations
        };
        
        const response = await axios.post(`${API_URL}/assign/asset`, assignmentData);
        
        // Reset form
        setSelectedEmployee('');
        setSelectedAsset('');
        setObservations('');
        setAssignmentDate(new Date().toISOString().split('T')[0]);
        
        // Show success message
        setSuccessMessage('Activo asignado correctamente.');
        setTimeout(() => {
            setSuccessMessage('');
        }, 5000);
        
        // Refresh available assets
        fetchData();
        
        setLoading(false);
        } catch (err) {
        setError('Error al asignar el activo: ' + (err.response?.data?.error || err.message));
        setLoading(false);
        console.error('Error assigning asset:', err);
        }
    };

    return (
        <div className="asset-assignment-container">
        <h2>Asignación de Activos</h2>
        
        {successMessage && (
            <div className="success-message">
            {successMessage}
            </div>
        )}
        
        {error && (
            <div className="error-message">
            {error}
            </div>
        )}
        
        <div className="assignment-form-container">
            <form onSubmit={handleSubmit} className="assignment-form">
            <div className="form-group">
                <label htmlFor="employee">Empleado</label>
                <select 
                id="employee" 
                value={selectedEmployee}
                onChange={(e) => setSelectedEmployee(e.target.value)}
                required
                disabled={loading}
                >
                <option value="">Seleccione un empleado</option>
                {employees.map(employee => (
                    <option key={employee.id} value={employee.id}>
                    {employee.fullName} - {employee.position}
                    </option>
                ))}
                </select>
            </div>
            
            <div className="form-group">
                <label htmlFor="asset">Activo</label>
                <select 
                id="asset" 
                value={selectedAsset}
                onChange={(e) => setSelectedAsset(e.target.value)}
                required
                disabled={loading}
                >
                <option value="">Seleccione un activo</option>
                {assets.map(asset => (
                    <option key={asset.id} value={asset.id}>
                    {asset.category} - {asset.brand} {asset.model} (SN: {asset.serialNumber})
                    </option>
                ))}
                </select>
            </div>
            
            <div className="form-group">
                <label htmlFor="assignmentDate">Fecha de Asignación</label>
                <input 
                type="date" 
                id="assignmentDate" 
                value={assignmentDate}
                onChange={(e) => setAssignmentDate(e.target.value)}
                required
                disabled={loading}
                />
            </div>
            
            <div className="form-group">
                <label htmlFor="observations">Observaciones</label>
                <textarea 
                id="observations" 
                value={observations}
                onChange={(e) => setObservations(e.target.value)}
                disabled={loading}
                rows="4"
                ></textarea>
            </div>
            
            <div className="form-actions">
                <button type="submit" className="button primary" disabled={loading}>
                {loading ? 'Procesando...' : 'Asignar Activo'}
                </button>
            </div>
            </form>
        </div>
        
        <div className="assignment-instructions">
            <h3>Instrucciones</h3>
            <ol>
            <li>Seleccione el empleado al que desea asignar el activo.</li>
            <li>Seleccione el activo disponible que desea asignar.</li>
            <li>Establezca la fecha de asignación (por defecto es la fecha actual).</li>
            <li>Añada observaciones relevantes si es necesario.</li>
            <li>Haga clic en "Asignar Activo" para finalizar el proceso.</li>
            </ol>
            <p><strong>Nota:</strong> Solo se muestran los activos con estado "Available" (Disponible).</p>
            <p>Una vez asignado, el activo cambiará automáticamente a estado "Assigned" (Asignado).</p>
        </div>
        </div>
    );
    }

export default AssetAssignment;