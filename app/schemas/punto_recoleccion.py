from pydantic import BaseModel
from typing import Optional
from datetime import date

class PuntoBase(BaseModel):
    Nombre: str
    Ubicacion: Optional[str]
    Latitud: Optional[float]
    Longitud: Optional[float]
    FechaCreacion: Optional[date]

class PuntoCreate(PuntoBase):
    pass

class PuntoUpdate(PuntoBase):
    pass

class PuntoOut(PuntoBase):
    Id: int

    class Config:
        orm_mode = True
