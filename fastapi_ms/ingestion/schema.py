from pydantic import BaseModel

class K4Score(BaseModel):
    name: str
    description: str
    formula: int

class K4ScoreRead(K4Score):
    id: int

    class Config:
        orm_mode = True
