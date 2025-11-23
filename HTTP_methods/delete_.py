from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name : str

@app.post('/users/{user_id}')
def create_user(user_id: int, user: User):
    return {"message": f"User {user.name} with ID {user_id} created"}

@app.get('/users/{user_id}')
def get_user(user_id: int):
    return{"message" : f"showing user {user_id}"}

@app.patch('/users/{user_id}')
def patch_user(user_id : int , user:User):
    return {"message" : f"User {user.name} with ID {user_id} partially updated"}

@app.put('/users/{user_id}')
def update_user(user_id : int , user:User):
    return {"message" : f" New User name {user.name} updated with same ID {user_id} successfully"}

@app.delete('/users/{user_id}')
def delete_user(user_id : int):
    return {"message" :  f"User with ID {user_id} deleted successfully"}