from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Item:
    concepto: str
    cantidad: float
    precio_unitario : float
    categoria_id: int
    id: Optional[int] = None

@dataclass
class Ticket:
    usuario_id : int
    establecimiento: str
    fecha: str
    items: List[Item]
    monto_total: Optional[float] = None
    notas: Optional[str] = None
    id: Optional[int] = None
    
    def __post_init__(self):
        if self.monto_total is None and self.items:
            self.monto_total = 0
            for item in self.items:
                self.monto_total += item.precio_unitario * item.cantidad