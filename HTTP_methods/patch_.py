from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name : str

@app.post('/users/{user_id}')
def create_user(user_id: int, user: User):
    return {"message": f"User {user.name} with ID {user_id} created"}



@app.patch('/users/{user_id}')
def patch_user(user_id : int , user:User):
    return {"message" : f"User {user.name} with ID {user_id} partially updated"}
