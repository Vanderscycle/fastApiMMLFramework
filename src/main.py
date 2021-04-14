from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:test@sql-db/testApi"

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    family = Column(String)
    description = Column(String)


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine, checkfirst=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from pydantic import BaseModel


class User(BaseModel):
    name: str
    family: str
    description: str

    class Config:
        orm_mode = True

from fastapi import FastAPI,Depends
from fastapi.encoders import jsonable_encoder

# API
app = FastAPI()


#GET
@app.get("/users/{userId}", response_model=User)
async def readUser(userId: int,db: Session = Depends(get_db)):
    _user = db.query(UserModel).get(userId)
    return _user

#POST
@app.post("/users/",response_model=User)
async def createUser(user:User,db: Session = Depends(get_db)):
    _user = UserModel(name = user.name,family =user.family,description = user.description)
    db.add(_user)
    print(_user)
    db.commit()
    db.refresh(_user)
    return _user
