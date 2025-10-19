from fastapi import FastAPI 

app = FastAPI()

@app.get("/items")
def get_items(name : str = None, price : int = None):
    return {"item_name" : name, "item_price":price}


