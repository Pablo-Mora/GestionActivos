from app.db.db import get_db
from app.models import AccesoWeb
from typing import List, Optional

def get_all_accesos() -> List[dict]:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AccesosWeb")
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return results

def get_acceso_by_id(id_acceso: int) -> Optional[dict]:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AccesosWeb WHERE Id = ?", id_acceso)
    row = cursor.fetchone()
    if row:
        columns = [column[0] for column in cursor.description]
        result = dict(zip(columns, row))
    else:
        result = None
    conn.close()
    return result

def create_acceso(acceso: AccesoWeb) -> None:
    conn = get_db()
    cursor = conn.cursor()
    query = """
        INSERT INTO AccesosWeb (EmpleadoId, URL, Usuario, Contrasena, ObligadoCambio)
        VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, acceso.EmpleadoId, acceso.URL, acceso.Usuario,
                   acceso.Contrasena, acceso.ObligadoCambio)
    conn.commit()
    conn.close()

def update_acceso(id_acceso: int, acceso: AccesoWeb) -> bool:
    conn = get_db()
    cursor = conn.cursor()
    query = """
        UPDATE AccesosWeb
        SET EmpleadoId=?, URL=?, Usuario=?, Contrasena=?, ObligadoCambio=?
        WHERE Id=?
    """
    cursor.execute(query, acceso.EmpleadoId, acceso.URL, acceso.Usuario,
                   acceso.Contrasena, acceso.ObligadoCambio, id_acceso)
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated

def delete_acceso(id_acceso: int) -> bool:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM AccesosWeb WHERE Id = ?", id_acceso)
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted
