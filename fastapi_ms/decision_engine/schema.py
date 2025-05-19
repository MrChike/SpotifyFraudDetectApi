from pydantic import BaseModel

class K2Score(BaseModel):
    name: str
    description: str
    formula: int

class K2ScoreRead(K2Score):
    id: int

    class Config:
        orm_mode = True
