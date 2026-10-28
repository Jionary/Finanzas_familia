from src.database.connection import get_connection
from src.models.gastos_fijos import GastoFijo
from typing import List

class GastoFijoRepository:
    def registrar_gasto(self, gasto_fijo: GastoFijo) -> int:
        with get_connection() as conn:
            gasto_registrar = (gasto_fijo.usuario_id, gasto_fijo.categoria_id, gasto_fijo.concepto, gasto_fijo.monto, gasto_fijo.frecuencia, gasto_fijo.dia_pago, gasto_fijo.activo)
            gasto_registrado = conn.execute("INSERT INTO gastos_fijos (usuario_id, categoria_id, concepto, monto, frecuencia, dia_pago, activo) VALUES (?,?,?,?,?,?,?)", gasto_registrar)
            gasto_fijo_id = gasto_registrado.lastrowid
        return gasto_fijo_id
    
    def obtener_gastos_activos(self) -> List[GastoFijo]:
        with get_connection() as conn:
            consulta_gastos = conn.execute("SELECT * FROM gastos_fijos WHERE activo = 1")
            gastos_extraidos = consulta_gastos.fetchall()
            gastos_activos = []
            if gastos_extraidos:
                for gasto in gastos_extraidos:
                    gastos_activos.append(GastoFijo(
                        id=gasto[0],
                        usuario_id=gasto[1],
                        categoria_id=gasto[2],
                        concepto=gasto[3],
                        monto=gasto[4],
                        frecuencia=gasto[5],
                        dia_pago=gasto[6],
                        activo=gasto[7]
                    ))
        return gastos_activos
    
    def obtener_gastos_usuario(self, usuario_id: int):
        with get_connection() as conn:
            consulta_gastos_fijos_usuario = conn.execute("SELECT * FROM gastos_fijos WHERE usuario_id = ? AND activo = 1", (usuario_id,))
            gastos_usuario_extraidos = consulta_gastos_fijos_usuario.fetchall()

        
        gastos_usuario = []
        for gasto in gastos_usuario_extraidos:
            gastos_usuario.append(GastoFijo(
                id=gasto[0],
                usuario_id=gasto[1],
                categoria_id=gasto[2],
                concepto=gasto[3],
                monto=gasto[4],
                frecuencia=gasto[5],
                dia_pago=gasto[6],
                activo=gasto[7]        
            ))
        return gastos_usuario
            

if __name__ == "__main__":
    repo = GastoFijoRepository()
    nuevo_gasto = GastoFijo(1,3, "Internet Infinitum", 599.99, 15)
    #repo.registrar_gasto(nuevo_gasto)
    print(repo.obtener_gastos_activos())