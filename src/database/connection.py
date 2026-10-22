import sqlite3 
from pathlib import Path

RUTA_ACTUAL = Path(__file__).resolve()
DB_PATH = RUTA_ACTUAL.parent.parent.parent/"data"/"finanzas.db"
SCHEMA_PATH = RUTA_ACTUAL.parent/"schema.sql"

def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as archivo:
        script_sql = archivo.read()
    with get_connection() as conexion:
        conexion.executescript(script_sql)
        
if __name__ == "__main__":
    init_db()
    print("¡Base de datos e historial de tablas creados con éxito!")