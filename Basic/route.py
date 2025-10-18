from fastapi import  FastAPI

app = FastAPI()

#endpoint 1
## route 1

@app.get('/')
def root():
    return ['hola🤧']

@app.get("/home")
def home():
    return {"message": "salam , its a home pages"}

## route 2
@app.get("/about")
def about():
    return {'message':"its a about section"}


