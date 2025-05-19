from pydantic import BaseModel

class K1Score(BaseModel):
    name: str
    description: str
    formula: int

class K1ScoreRead(K1Score):
    id: int

    class Config:
        orm_mode = True
