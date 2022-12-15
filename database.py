from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

DataBaseURL = "mysql+mysqlconnector://root:Temp1234@localhost:3306/Todo"

engine = create_engine(DataBaseURL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine) 

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


