from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmpresaBase(BaseModel):
    Nombre: str
    Ubicacion: Optional[str]
    Correo: Optional[str]
    Telefono: Optional[int]
    FechaCreacion: Optional[date]

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaUpdate(EmpresaBase):
    pass

class EmpresaOut(EmpresaBase):
    Id: int

    class Config:
        orm_mode = True
