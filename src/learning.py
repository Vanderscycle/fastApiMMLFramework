import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
# data validation
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    Name: str
    Family: str
    Description: str

    class Config:
        orm_mode = True

names = ["Joe", "Bobby", 'Keanu']
families = ["Baldwin","Gilpin","Reeves"]
descriptions = ["Family that loves to scream Joe Baldwin every chance they get",
                "Mega sailor",
                "You are breathtaking"]

sampleData = dict()
for n,f,d in zip(names,families,descriptions):
    ID=len(sampleData)
    sampleData[ID] = (
        User(
            Name=n,
            Family=f,
            Description=d
            )
        )
print(sampleData)

# homepage 
@app.get("/")
async def root():
    return {"message": "Hello World"}

# GET
@app.get("/users/{userId}", response_model=User)
async def readUser(userId: int):
    return sampleData[userId]

@app.get("/users/")
async def giveAllUser():
    output = list()
    for k,v in sampleData.items():
        # not a perfect solution considering that the sample data index the key of the dict
        output.append([k,jsonable_encoder(v)])
    return output

@app.post("/users/",response_model=User)
async def createUser(user:User):
    sampleData[len(sampleData)] = user
    return user

@app.delete("/users/{userId}")
async def deleteUser(userId: int):
    tempData = sampleData[userId]
    print(f"deleting {tempData}")
    del sampleData[userId]
    # we will need to reindex the data, I think its better when done at the db level
    return {"message": f"User {tempData.Name} {tempData.Family} has been deleted"}

@app.patch("/users/{userId}", response_model=User)
async def patchUser(userId: int,replacementData: User):
    storedItemData = dict(sampleData[userId])
    print(storedItemData)
    updateData = replacementData.dict()
    print(updateData)
    for k,v in updateData.items():
        # make shift solution not very scalable (for different dtypes)
        # need to find a way that takes in account the class default dtype
        if v != 'string':
            storedItemData[k] = v

    sampleData[userId] = jsonable_encoder(storedItemData)
    return {'message': f" data updated: {sampleData[userId]}"}

