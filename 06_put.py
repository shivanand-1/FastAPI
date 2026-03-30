from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name:  str
    email: EmailStr
app=FastAPI()
users_db = {}
next_id  = 1

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    global next_id

    # Duplicate check
    for u in users_db.values():
        if u["email"] == user.email:
            raise HTTPException(
                status_code=409,
                detail="Email already registered"
            )

    users_db[next_id] = {"id": next_id, **user.dict()}
    created = users_db[next_id]
    next_id += 1
    return created