from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Bitacora(Base):
    __tablename__ = "bitacora"

    Id = Column(Integer, primary_key=True, index=True)
    Usuario = Column(String(255), nullable=False)
    Accion = Column(String(100), nullable=False)
    Modulo = Column(String(100), nullable=False)
    Detalles = Column(String(1000), nullable=True)
    Fecha = Column(DateTime, server_default=func.now(), nullable=False)
