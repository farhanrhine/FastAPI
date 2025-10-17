# main.py
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# A simple route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}