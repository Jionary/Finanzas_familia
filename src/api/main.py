from fastapi import FastAPI
from src.analytics.resumen import ResumenService
from typing import Dict, Any
from src.models.tickets import Ticket, Item
from src.database.tickets import TicketRepository
from src.api.schemas.tickets import TicketCreate
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="API de Finanzas Familiares",
    description="Esta es la api de mi proyecto para ayudar a mis papas con sus finanzas",
    version="1.0.0"
    )
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
resumen = ResumenService()
ticket_repo = TicketRepository()

@app.get("/")
def health() -> Dict[str, Any]:
    return {"Mensaje": "Funciona correctamente:)"}

@app.get("/api/v1/resumen")
def get_resumen(mes: int, ano: int) -> Dict[str,Any]:
    return resumen.resumen_mensual(mes=mes, ano=ano)

@app.get("/api/v1/tickets/{ticket_id}")
def obtener_por_id(ticket_id: int) -> Dict[str, Any]:
    ticket_obtenido = ticket_repo.obtener_por_id(ticket_id)
    return {"Tu ticket obtenido fue: ": ticket_obtenido}

@app.post("/api/v1/tickets") 
def crear_ticket(ticket_in: TicketCreate) -> Dict[str,Any]:
    items = []
    for item in ticket_in.items:
        items.append(Item(
            concepto=item.concepto,
            cantidad=item.cantidad,
            precio_unitario=item.precio_unitario,
            categoria_id=item.categoria_id
            ))
    ticket_guardar = Ticket(
        usuario_id=1,
        establecimiento=ticket_in.establecimiento,
        fecha=ticket_in.fecha,
        items=items)
    ticket_id = ticket_repo.guardar(ticket_guardar)
    return {"Tu ticket se guardo con éxito y tiene el id" : ticket_id}




    