# https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

import jsbeautifier
import json

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:test@sql-db/testApi"
testing = True

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    family = Column(String)
    description = Column(String)


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# deletes the previous data since we are still testing
if testing:
    Base.metadata.drop_all(bind=engine, tables=[UserModel.__table__])
Base.metadata.create_all(engine, checkfirst=True, )


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

#HOMEPAGE
@app.get("/")
async def root():
    return {"message": "Hello World"}

#GET
@app.get("/users/{userId}", response_model=User)
async def readUser(userId: int,db: Session = Depends(get_db)):
    # I have no clue why userId start at 1 instead of 0
    _user = db.query(UserModel).get(userId)
    #inspector = inspect(engine)
    #print(inspector.get_columns('user'))
    try:
        return _user
    except Exception as e:
        return {"message": e}


#GETALL
@app.get("/users/")
async def giveAllUser(db: Session = Depends(get_db)):
    _users = db.query(UserModel).all()

    allUsers = list()

    for _user in _users:
        try:
            allUsers.append({"id":_user.id,"name":_user.name,"family":_user.family,"description":_user.description})

        except Exception as e:
            print(e)
        #outDict[_user.id] = jsonable_encoder(_user) 
    allUsers.sort(key = lambda allUsers:allUsers["id"])
    opts = jsbeautifier.default_options()
    opts.indent_size =2
    return jsbeautifier.beautify(json.dumps(allUsers), opts)


#POST
@app.post("/users/",response_model=User)
async def createUser(user:User,db: Session = Depends(get_db)):
    _user = UserModel(name = user.name,family =user.family,description = user.description)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


#DELETE
#Known issues (choosing the  first available id)
@app.delete("/users/{userId}")
async def deleteUser(userId:int,db: Session = Depends(get_db)):
    db.query(UserModel).filter(UserModel.id==userId).delete()
    try:
        db.commit()
        return {"message": f"userId {userId} delete"}
    except Exception:
        return {"message": f"userId {userId} does not exist"}


# PATCH
@app.patch("/users/{userId}",response_model=User)
async def patchUser(userId:int, replacementData: User, db: Session = Depends(get_db)):
    _user = db.query(UserModel).get(userId)
    updateData = replacementData.dict()
    dictUser = {"id":_user.id,"name":_user.name,"family":_user.family,"description":_user.description}

    # need to find a way to use the default dtype to compare
    for k,v in updateData.items():
        if v != 'string':
            dictUser[k] = v
    # not scalable, need more time with pydantic
    db.query(UserModel).filter(UserModel.id == userId).update({UserModel.name:dictUser["name"],UserModel.family:dictUser["family"],UserModel.description:dictUser["description"]})
    db.commit()
    return dictUser
