from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class EmpresaTipoReciclaje(Base):
    __tablename__ = "empresa_tiporeciclaje"

    Id = Column(Integer, primary_key=True, index=True)
    id_Empresa = Column(Integer, ForeignKey("empresa.Id", ondelete="CASCADE"), nullable=False)
    id_TipoReciclaje = Column(Integer, ForeignKey("tiposreciclaje.Id", ondelete="CASCADE"), nullable=False)

    empresa = relationship("Empresa", back_populates="tipos_reciclaje")
