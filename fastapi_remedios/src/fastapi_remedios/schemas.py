from pydantic import BaseModel
from typing import Optional

class RemedioBase(BaseModel):
    nome: str
    horario: str
    dosagem: str
    observacoes: Optional[str] = None

class RemedioCreate(RemedioBase):
    pass

class RemedioUpdate(RemedioBase):
    pass

class RemedioOut(RemedioBase):
    id: int

    class Config:
        orm_mode = True
