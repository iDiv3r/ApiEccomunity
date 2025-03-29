from pydantic import BaseModel
from datetime import time, date
from typing import Optional

class HorarioBase(BaseModel):
    hora_inicio: time
    hora_final: time
    dia: str
    id_PuntoRecoleccion: int
    FechaCreacion: Optional[date]

class HorarioCreate(HorarioBase):
    pass

class HorarioUpdate(HorarioBase):
    pass

class HorarioOut(HorarioBase):
    Id: int

    class Config:
        orm_mode = True
