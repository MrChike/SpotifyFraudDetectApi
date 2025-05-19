from sqlalchemy import Column, Integer, String
from shared.db.connection import Base


class K4Score(Base):
    __tablename__ = "k4_scores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    formula = Column(Integer, nullable=False)