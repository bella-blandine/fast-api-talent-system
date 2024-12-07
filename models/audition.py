
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Audition(Base):
    __tablename__ = "auditions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    judge_id = Column(Integer, ForeignKey("judges.id"))

    judge = relationship("Judge", back_populates="auditions")
