from Backend.app.Db.db import get_connection
from Backend.app.models.models import Aprobacion
from typing import List, Optional

def get_all_aprobaciones() -> List[dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Aprobaciones")
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return results

def get_aprobacion_by_id(id_aprobacion: int) -> Optional[dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Aprobaciones WHERE Id = ?", id_aprobacion)
    row = cursor.fetchone()
    if row:
        columns = [column[0] for column in cursor.description]
        result = dict(zip(columns, row))
    else:
        result = None
    conn.close()
    return result

def create_aprobacion(aprobacion: Aprobacion) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO Aprobaciones (EmpleadoId, AprobadoPor, CargoAprobador)
        VALUES (?, ?, ?)
    """
    cursor.execute(query, aprobacion.EmpleadoId, aprobacion.AprobadoPor, aprobacion.CargoAprobador)
    conn.commit()
    conn.close()

def update_aprobacion(id_aprobacion: int, aprobacion: Aprobacion) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE Aprobaciones
        SET EmpleadoId=?, AprobadoPor=?, CargoAprobador=?
        WHERE Id=?
    """
    cursor.execute(query, aprobacion.EmpleadoId, aprobacion.AprobadoPor,
                   aprobacion.CargoAprobador, id_aprobacion)
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated

def delete_aprobacion(id_aprobacion: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Aprobaciones WHERE Id = ?", id_aprobacion)
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted
