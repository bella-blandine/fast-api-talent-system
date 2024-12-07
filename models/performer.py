
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class Performer(Base):
    __tablename__ = "performers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)

    performances = relationship("Performance", back_populates="performer")
