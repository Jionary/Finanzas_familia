from src.database.connection import get_connection
from src.models.categories import Categorias
from typing import List


class CategoriesRepository:
    def guardar(self, categoria:Categorias) -> int:
        with get_connection() as conn:
            categoria_nueva = conn.execute("INSERT INTO categorias (nombre, tipo) VALUES (?,?)", (categoria.nombre, categoria.tipo))
        return categoria_nueva.lastrowid
    
    def obtener_todas(self) -> List[Categorias]:
        with get_connection() as conn:
            categorias_consultadas = conn.execute("SELECT * FROM categorias")
            categorias_obtenidas = categorias_consultadas.fetchall()
            categorias = []
            for categoria in categorias_obtenidas:
                categorias.append(
                    Categorias(
                        id=categoria[0],
                        nombre=categoria[1],
                        tipo=categoria[2]))
        return categorias
if __name__ == "__main__":
    repo = CategoriesRepository()
    
    # 1. Guardar una nueva
    nueva_cat = Categorias(nombre="Mascotas", tipo="GASTO")
    cat_id = repo.guardar(nueva_cat)
    print(f"Categoría guardada con ID: {cat_id}")
    
    # 2. Leer todas
    todas = repo.obtener_todas()
    print(f"\nTotal de categorías en la BD: {len(todas)}")
    for c in todas:
        print(f"  [{c.id}] {c.nombre} ({c.tipo})")