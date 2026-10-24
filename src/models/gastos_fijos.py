from dataclasses import dataclass
from typing import Optional


@dataclass
class GastoFijo:
    usuario_id: int
    categoria_id: int
    concepto: str
    monto: float
    dia_pago: int
    id: Optional[int] = None
    frecuencia: Optional[str] = "MENSUAL"
    activo: Optional[int] = 1