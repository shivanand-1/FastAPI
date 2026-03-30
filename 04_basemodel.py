from fastapi import FastAPI
from pydantic import BaseModel,EmailStr, Field
from typing import Optional

app=FastAPI()
class series(BaseModel):
    #in enum you can make the  = but not in the basemodel
    id:int=Field(ge=18, le=120)#for int you can use the ge and le
    name:str=Field(min_length=2,max_length=20) #fir the string you can use the min_length and max length 
    gmail:EmailStr
    age:Optional[str]

user = series(age="3")# Automatically converts to int 
class Address(BaseModel):
    street: str
    city:   str
    pin:    str

class UserWithAddress(BaseModel):
    name:    str
    email:   EmailStr
    address: Address   # nested

@app.post("/users/full")
def create_full_user(user: UserWithAddress):
    return user