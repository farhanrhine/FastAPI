from fastapi import FastAPI

app = FastAPI()

@app.get('/users/{user_id}')
def get_user(user_id: int):
    return{"message" : f"showing user {user_id}"}