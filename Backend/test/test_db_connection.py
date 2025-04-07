import pyodbc

def test_connection():
    try:
        connection = pyodbc.connect(
            'DRIVER = {ODBC Driver 17 for SQL Server};'
            'SERVER = AUXCONTA\\SQLEXPRESS;'
            'DATABASE = GestionActivos;'
            'Trusted_Connection=yes;'
        )
        print("✅ Conexión exitosa a SQL Server.")
        connection.close()
    except Exception as e:
        print("❌ Error al conectar:", e)

if __name__ == "__main__":
    test_connection()