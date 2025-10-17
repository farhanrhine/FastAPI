# main.py
from fastapi import FastAPI

# Create an instance/obj of the FastAPI class, so "app" handle all incoming web requests
app = FastAPI()
farhan = FastAPI()

# A simple route
@app.get("/") # The @ syntax is just a shortcut for a regular function call.
def read_root():
    return {"message": "salam, FastAPI!"}

@farhan.get("/home")
def root():
    return ('its farhan')
# http://127.0.0.1:8000/docs#/default/root__get >>> if ("/")
# http://127.0.0.1:8000/docs#/default/rootfar_get >>> if ("far")
# http://127.0.0.1:8000/docs#/default/root_home_get >>> if ("home")