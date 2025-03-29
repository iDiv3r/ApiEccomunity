from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BitacoraBase(BaseModel):
    Usuario: str
    Accion: str
    Modulo: str
    Detalles: Optional[str]

class BitacoraCreate(BitacoraBase):
    pass

class BitacoraOut(BitacoraBase):
    Id: int
    Fecha: datetime

    class Config:
        orm_mode = True
