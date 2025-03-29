from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class RecoleccionEmpresa(Base):
    __tablename__ = "recoleccion_empresa"

    Id = Column(Integer, primary_key=True, index=True)
    Hora = Column(Time, nullable=False)
    Dia = Column(String(50), nullable=False)
    id_Empresa = Column(Integer, ForeignKey("empresa.Id", ondelete="CASCADE"), nullable=False)
    id_PuntoRecoleccion = Column(Integer, ForeignKey("puntosrecoleccion.Id", ondelete="CASCADE"), nullable=False)

    empresa = relationship("Empresa", back_populates="recolecciones_empresa")
    