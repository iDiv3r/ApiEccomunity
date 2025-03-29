from pydantic import BaseModel
from typing import Optional
from datetime import time

class RecoleccionBase(BaseModel):
    Tipo: int
    Dia: str
    Hora: time
    Cantidad: str
    Status: str
    id_PuntoRecoleccion: int
    id_Usuario: int

class RecoleccionCreate(RecoleccionBase):
    pass

class RecoleccionUpdate(RecoleccionBase):
    pass

class RecoleccionOut(RecoleccionBase):
    Id: int

    class Config:
        orm_mode = True
