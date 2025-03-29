from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Medalla(Base):
    __tablename__ = "medallas"

    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    color = Column(String(20), nullable=False)

    id_usuario = Column(Integer, ForeignKey("usuarios.Id", ondelete="CASCADE"), nullable=False)
    usuario = relationship("Usuario", back_populates="medallas")
