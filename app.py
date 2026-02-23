from sqlalchemy.orm import sessionmaker
from model import Table
from database import Base, engine

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

user01 = Table(username="keyur344", password=123)
session.add(user01)

session.commit()
