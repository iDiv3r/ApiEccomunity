from sqlalchemy import Column, Integer, String
from app.database import Base

class TipoReciclaje(Base):
    __tablename__ = "tiposreciclaje"

    Id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100), nullable=False, unique=True)
