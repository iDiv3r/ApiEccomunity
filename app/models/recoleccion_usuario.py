from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class RecoleccionUsuario(Base):
    __tablename__ = "recoleccionesusuarios"

    Id = Column(Integer, primary_key=True, index=True)
    Tipo = Column(Integer, nullable=False)
    Dia = Column(String(50), nullable=False)
    Hora = Column(Time, nullable=False)
    Cantidad = Column(String(100), nullable=False)
    Status = Column(String(50), nullable=False)
    id_PuntoRecoleccion = Column(Integer, ForeignKey("puntosrecoleccion.Id", ondelete="CASCADE"), nullable=False)
    id_Usuario = Column(Integer, ForeignKey("usuarios.Id", ondelete="CASCADE"), nullable=False)

    usuario = relationship("Usuario", back_populates="recolecciones")
