from Backend.app.Db.db import get_connection
from Backend.app.models.models import ResponsableEntrega
from typing import List, Optional

def get_all_responsables() -> List[dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ResponsablesEntrega")
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return results

def get_responsable_by_id(id_responsable: int) -> Optional[dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ResponsablesEntrega WHERE Id = ?", id_responsable)
    row = cursor.fetchone()
    if row:
        columns = [column[0] for column in cursor.description]
        result = dict(zip(columns, row))
    else:
        result = None
    conn.close()
    return result

def create_responsable(responsable: ResponsableEntrega) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO ResponsablesEntrega (EmpleadoId, Recibe, Entrega, RolRecibe, RolEntrega)
        VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, responsable.EmpleadoId, responsable.Recibe, responsable.Entrega,
                   responsable.RolRecibe, responsable.RolEntrega)
    conn.commit()
    conn.close()

def update_responsable(id_responsable: int, responsable: ResponsableEntrega) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE ResponsablesEntrega
        SET EmpleadoId=?, Recibe=?, Entrega=?, RolRecibe=?, RolEntrega=?
        WHERE Id=?
    """
    cursor.execute(query, responsable.EmpleadoId, responsable.Recibe, responsable.Entrega,
                   responsable.RolRecibe, responsable.RolEntrega, id_responsable)
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated

def delete_responsable(id_responsable: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ResponsablesEntrega WHERE Id = ?", id_responsable)
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted