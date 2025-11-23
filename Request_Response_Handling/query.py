from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items(name: str = None, price: int = None): # type: ignore
    return {"item_name": name, "item_price": price}



# Query parameters come after ? in the URL
# http://127.0.0.1:8000/items?name=mango&price=100