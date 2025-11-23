# body or requst parameters are used to send more complex data structures like JSON objects in the request body.
from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

class User(BaseModel):
    name : str
    age : int
    email : str

@app.post("/create_user")
def create_user(user:User):
    return {"message": f"User Name : {user.name}, Age : {user.age}, Email : {user.email} created successfully"}