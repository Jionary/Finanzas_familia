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
        categorias_2 = {
            ("Renta", "GASTO"),
            ("Otros", "GASTO")
        }
        """conn.executemany("INSERT INTO usuarios (nombre) VALUES (?)", usuarios)
        conn.executemany("INSERT INTO categorias (nombre, tipo) VALUES (?, ?)", categorias)"""
        conn.executemany("INSERT INTO categorias (nombre, tipo) VALUES (?, ?)", categorias_2)

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
        #conn.execute("UPDATE categorias SET tipo = ? WHERE nombre = ?", ("INGRESO", "Sueldo"))
        """conn.execute("UPDATE categorias SET id = 7 WHERE id = 9")
        conn.execute("UPDATE categorias SET id = 8 WHERE id = 10")"""
        conn.execute("UPDATE sqlite_sequence SET seq = 8 WHERE name = 'categorias'")

def delete_datos():
    with get_connection() as conn:
        conn.execute("DELETE FROM categorias WHERE id IN (1,2,3,4,5,6,9,10)")

if __name__ == "__main__":
   #poblar_datos_iniciales()
    modificar_datos()
    #verificar_datos()
   #delete_datos()
   