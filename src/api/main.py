from fastapi import FastAPI
from src.analytics.resumen import ResumenService
from typing import Dict, Any
from src.models.tickets import Ticket, Item
from src.models.gastos_fijos import GastoFijo
from src.database.tickets import TicketRepository
from src.database.gastos_fijos import GastoFijoRepository
from src.database.categories import CategoriesRepository
from src.api.schemas.tickets import TicketCreate
from src.api.schemas.gastos_fijos import GastoCreate
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
gastos_repo = GastoFijoRepository()
categorias_repo = CategoriesRepository()

@app.get("/")
def health() -> Dict[str, Any]:
    return {"Mensaje": "Funciona correctamente:)"}

@app.get("/api/v1/resumen")
def get_resumen(mes: int, ano: int) -> Dict[str,Any]:
    return resumen.resumen_mensual(mes=mes, ano=ano)


@app.get("/api/v1/resumen/usuario/{usuario_id}")
def get_resumen_usuario(mes: int, ano: int, usuario_id: int) -> Dict[str, Any]:
    return resumen.resumen_mensual_usuario(mes=mes, ano=ano, usuario_id=usuario_id)


@app.get("/api/v1/tickets/{ticket_id}")
def obtener_por_id(ticket_id: int) -> Dict[str, Any]:
    ticket_obtenido = ticket_repo.obtener_por_id(ticket_id)
    return {"Tu ticket obtenido fue: ": ticket_obtenido}

@app.get("/api/v1/categorias")
def obtener_todas_categorias() -> Dict[str, Any]:
    categorias_obtenidas = categorias_repo.obtener_todas()
    return {"Tus categorias son: ": categorias_obtenidas}

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
        usuario_id=ticket_in.usuario_id,
        establecimiento=ticket_in.establecimiento,
        fecha=ticket_in.fecha,
        items=items)
    ticket_id = ticket_repo.guardar(ticket_guardar)
    return {"Tu ticket se guardo con éxito y tiene el id" : ticket_id}

@app.post("/api/v1/gastos")
def crear_gasto(gasto_in: GastoCreate) -> Dict[str, Any]:
    gasto_guardar = GastoFijo(
        usuario_id=gasto_in.usuario_id,
        categoria_id=gasto_in.categoria_id,
        concepto=gasto_in.concepto,
        monto=gasto_in.monto,
        dia_pago=gasto_in.dia_pago,
        frecuencia=gasto_in.frecuencia,
        activo=1)
    gasto_id = gastos_repo.registrar_gasto(gasto_guardar)
    return {"Tu gasto se ha guardado con éxito y su id:" : gasto_id}



    