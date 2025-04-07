import os
import secrets
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = secrets.token_hex(16)

    # Carpetas de subida/descarga
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'uploads')
    DOWNLOAD_FOLDER = os.path.join(os.path.dirmane(os.path.dirname(__file__)), 'static', 'downloads')
    ALLOWED_EXTENSIONS = {'doxs', 'xlsx'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 #16MB

    # Configuración de la base de datos:
    DB_CONFIG = {
        "driver": os.getenv("DB_DRIVER"),
        "server": os.getenv("DB_SERVER"),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "use_windows_auth": os.getenv("USE_WINDOWS_AUTH", "false").lower() == "true"
    }