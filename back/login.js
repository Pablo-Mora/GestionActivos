import React, { useState } from 'react';
import axios from 'axios';
import './Login.css';

const API_URL = 'http://localhost:5000/api';

function Login({ onLogin }) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            // En un sistema real, este endpoint debería verificar las credenciales
            // Por ahora, simularemos un inicio de sesión exitoso
            const mockUserData = {
            id: 1,
            username: username,
            role: 'admin',
            name: 'Administrador de TI'
            };
            
            // Simulamos un tiempo de espera para la autenticación
            setTimeout(() => {
                onLogin(mockUserData);
                setLoading(false);
            }, 1000);
            
            // En una implementación real, usaríamos algo como:
            // const response = await axios.post(`${API_URL}/login`, { username, password });
            // onLogin(response.data);
        } catch (err) {
            setError('Error en la autenticación. Verifica tus credenciales.');
            setLoading(false);
            console.error('Error de inicio de sesión:', err);
        }
    };

    return (
    <div className="login-container">
        <div className="login-card">
            <h2>Iniciar Sesión</h2>
            <form onSubmit={handleSubmit} className="login-form">
            {error && <p className="error-message">{error}</p>}
            
            <div className="form-group">
                <label htmlFor="username">Usuario</label>
                <input
                type="text"
                id="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
                />
            </div>
            
            <div className="form-group">
                <label htmlFor="password">Contraseña</label>
                <input
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                />
            </div>
            
            <button type="submit" className="login-button" disabled={loading}>
                {loading ? 'Iniciando sesión...' : 'Iniciar Sesión'}
            </button>
            </form>
        </div>
        </div>
    );
}

export default Login;