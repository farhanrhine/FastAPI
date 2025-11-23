from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}") # {user_id} in path = function parameter name, Path parameters are values inside the URL path
def get_user(user_id : int):
    return {"message": f"User ID is {user_id}"}
