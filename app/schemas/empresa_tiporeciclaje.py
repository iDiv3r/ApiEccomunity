from pydantic import BaseModel

class AsignacionTipo(BaseModel):
    id_Empresa: int
    id_TipoReciclaje: int

class AsignacionOut(AsignacionTipo):
    Id: int

    class Config:
        orm_mode = True
