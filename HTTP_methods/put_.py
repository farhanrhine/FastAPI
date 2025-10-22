from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name : str
    age : int

@app.post("/users")
def create_user(user:User):
    return{"message": f"User {user.name} created"}



@app.put('/users/{user_id}')
def update_user(user_id : int , user:User):
    return {"message" : f"{user_id} name update {user.name}"}
