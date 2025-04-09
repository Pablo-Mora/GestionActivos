import pyodbc
import os
from dotenv import load_dotenv

# Cargar las variables desde .env
load_dotenv()

def test_connection():
    try:
        connection_str = (
            f'DRIVER={{{os.getenv("DB_DRIVER")}}};'
            f'SERVER={os.getenv("DB_SERVER")};'
            f'DATABASE={os.getenv("DB_NAME")};'
            f'UID={os.getenv("DB_USER")};'
            f'PWD={os.getenv("DB_PASSWORD")};'
            'Trusted_Connection=no;'
        )
        connection = pyodbc.connect(connection_str)
        print("✅ Conexión exitosa a SQL Server.")
        connection.close()
    except Exception as e:
        print("❌ Error al conectar:", e)

if __name__ == "__main__":
    test_connection()
