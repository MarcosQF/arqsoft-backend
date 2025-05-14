from sqlalchemy import Column, Integer, String
from fastapi_remedios.database import Base

class Remedio(Base):
    __tablename__ = "remedios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    horario = Column(String, nullable=False)
    dosagem = Column(String, nullable=False)
    observacoes = Column(String, nullable=True)
