from sqlalchemy import Column, Integer, String
from database import Base

class Software(Base):
    __tablename__ = "software"

    id = Column(Integer, primary_key=True, index=True)
    machine = Column(String)
    name = Column(String)
    version = Column(String)
