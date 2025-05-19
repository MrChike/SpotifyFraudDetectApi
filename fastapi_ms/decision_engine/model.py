from sqlalchemy import Column, Integer, String
from shared.db.connection import Base


class K2Score(Base):
    __tablename__ = "k2_scores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    formula = Column(Integer, nullable=False)