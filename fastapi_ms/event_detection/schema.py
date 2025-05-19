from pydantic import BaseModel

class K3Score(BaseModel):
    name: str
    description: str
    formula: int

class K3ScoreRead(K3Score):
    id: int

    class Config:
        orm_mode = True
