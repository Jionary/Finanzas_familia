from pydantic import BaseModel

class GastoCreate(BaseModel):
    usuario_id: int
    categoria_id: int
    concepto: str
    monto: float
    frecuencia: str
    dia_pago: int
    activo: int
    
