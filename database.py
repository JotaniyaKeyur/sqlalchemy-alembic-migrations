from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///mydb.db"

engine = create_engine(db_url, echo=True)

Base = declarative_base() 
