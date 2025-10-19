from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

class User(BaseModel):
    name : str
    age : int
    email : str

@app.post("/create_user")
def create_user(user:User):
    return {"message": f"User {user.name} created successfully"}