from dataclasses import dataclass
from typing import Optional

@dataclass
class Categorias:
    nombre: str
    tipo: str
    id: Optional[int] = None
    