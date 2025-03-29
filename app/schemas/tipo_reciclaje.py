from pydantic import BaseModel

class TipoReciclajeBase(BaseModel):
    Nombre: str

class TipoReciclajeCreate(TipoReciclajeBase):
    pass

class TipoReciclajeUpdate(TipoReciclajeBase):
    pass

class TipoReciclajeOut(TipoReciclajeBase):
    Id: int

    class Config:
        orm_mode = True
