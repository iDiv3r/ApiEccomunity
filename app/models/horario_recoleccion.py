from sqlalchemy import Column, Integer, Time, String, Date, ForeignKey
from app.database import Base

class HorarioRecoleccion(Base):
    __tablename__ = "horarios_recoleccion"

    Id = Column(Integer, primary_key=True, index=True)
    hora_inicio = Column(Time, nullable=False)
    hora_final = Column(Time, nullable=False)
    dia = Column(String(50), nullable=False)
    id_PuntoRecoleccion = Column(Integer, ForeignKey("puntosrecoleccion.Id"), nullable=False)
    FechaCreacion = Column(Date, nullable=True)
