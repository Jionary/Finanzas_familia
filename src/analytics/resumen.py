from src.database.tickets import TicketRepository
from src.database.gastos_fijos import GastoFijoRepository
from typing import Dict, Any

class ResumenService:
    def __init__(self) -> None:
        self.ticket_repository = TicketRepository()
        self.gasto_fijo_repository = GastoFijoRepository()

    def resumen_mensual(self, mes:int, ano: int) -> Dict[str, Any]:
        resumen_mensual_fijo = 0
        resumen_mensual_tickets = 0
        for gasto in self.gasto_fijo_repository.obtener_gastos_activos():
            resumen_mensual_fijo += gasto.monto
        
        for ticket in self.ticket_repository.obtener_por_mes(mes, ano):
            resumen_mensual_tickets += ticket.monto_total

        resumen_mensual = resumen_mensual_tickets + resumen_mensual_fijo
        return {
            "Mes": mes,
            "Año": ano,
            "Gastos Fijos": resumen_mensual_fijo,
            "Gastos Tickets": resumen_mensual_tickets,
            "Total general": resumen_mensual
        }
    
if __name__ == "__main__":
    resumen = ResumenService()
    print(resumen.resumen_mensual(mes=10, ano=2026))