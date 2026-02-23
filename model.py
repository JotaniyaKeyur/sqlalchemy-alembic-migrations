from sqlalchemy import Column, Integer, String
from database import Base, engine

class Table(Base):
    __tablename__ = "user"

    fullname = Column(String)
    password = Column(Integer, primary_key=True)
