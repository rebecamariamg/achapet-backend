from sqlalchemy import Column, Integer, String
from app.utils.database import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    localizacao = Column(String, index=True)
    telefone = Column(String, index=True)
    categoria = Column(String, index=True) 
    tipo = Column(String, index=True)
    image_path = Column(String, nullable=True) 

