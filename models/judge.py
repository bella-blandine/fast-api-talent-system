
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class Judge(Base):
    __tablename__ = "judges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)

    auditions = relationship("Audition", back_populates="judge")
