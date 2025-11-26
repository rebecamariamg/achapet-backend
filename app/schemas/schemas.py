from pydantic import BaseModel
from typing import Optional

class PetBase(BaseModel):
    nome: str
    localizacao: str
    telefone: str
    categoria: str 
    tipo: Optional[str] = None
    
class PetCreate(PetBase):
    pass

class PetUpdate(BaseModel):
    nome: Optional[str]
    localizacao: Optional[str]
    telefone: Optional[str]
    categoria: Optional[str]
    tipo: Optional[str]


class Pet(PetBase):
    id: int
    image_path: Optional[str] = None

    class Config:
        from_attributes = True