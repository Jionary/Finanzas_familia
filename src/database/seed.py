from connection import get_connection

def poblar_datos_iniciales():
    with get_connection() as conn:
        usuarios = [("Papa",),("Mama",), ("Jio",)]
        categorias = [
            ("Supermercado", "GASTO"),
            ("Servicios", "GASTO"),
            ("Entretenimiento", "GASTO"),
            ("Salud", "GASTO"),
            ("Sueldo", "INGRESO")
        ]
        conn.executemany("INSERT INTO usuarios (nombre) VALUES (?)", usuarios)
        conn.executemany("INSERT INTO categorias (nombre, tipo) VALUES (?, ?)", categorias)

def verificar_datos():
    with get_connection() as conn:
        cursor_usuarios = conn.execute("SELECT * FROM usuarios")
        usuarios_guardados = cursor_usuarios.fetchall()
        cursor_categorias = conn.execute("SELECT * FROM categorias")
        categorias_guardadas = cursor_categorias.fetchall()
        print("Estos son tus usuarios guardados: ")
        print(usuarios_guardados)
        print("Estas son las categorias guardadas:")
        print(categorias_guardadas)

def modificar_datos():
    with get_connection() as conn:
        conn.execute("UPDATE categorias SET tipo = ? WHERE nombre = ?", ("INGRESO", "Sueldo"))

if __name__ == "__main__":
    #poblar_datos_iniciales()
    modificar_datos()
    verificar_datos()