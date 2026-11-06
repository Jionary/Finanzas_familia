from pydantic import BaseModel
from typing import Optional, List

class ItemCreate(BaseModel):
    categoria_id: int
    concepto: str
    cantidad: int
    precio_unitario: float
    
class TicketCreate(BaseModel):
    usuario_id: int
    establecimiento: str
    fecha: str
    notas: Optional[str]
    items: List[ItemCreate]
    