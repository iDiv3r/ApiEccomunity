from pydantic import BaseModel
from datetime import time

class RecoleccionEmpresaBase(BaseModel):
    Hora: time
    Dia: str
    id_Empresa: int
    id_PuntoRecoleccion: int

class RecoleccionEmpresaCreate(RecoleccionEmpresaBase):
    pass

class RecoleccionEmpresaUpdate(RecoleccionEmpresaBase):
    pass

class RecoleccionEmpresaOut(RecoleccionEmpresaBase):
    Id: int

    class Config:
        orm_mode = True
