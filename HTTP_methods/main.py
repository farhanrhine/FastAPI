from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

class User(BaseModel):
    name: str = Field(..., description="The user's full name")
    age: int = Field(..., ge=18, le=99, description="User's age (must be between 18 and 99)")
    email: Optional[str] = None  # Optional field
    hobbies: List[str] = []      # List with a default value

@app.post("/users/")
def create_user(user: User):
    return {"message": "User created!", "user_data": user}
