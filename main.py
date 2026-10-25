from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ========== Basic Route ==========
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# ========== Path Parameter ==========
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# ========== Query Parameter ==========
@app.get("/search")
def search(q: str = None, limit: int = 10):
    return {"query": q, "limit": limit}

# ========== Request Body Model (POST) ==========
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}

# ========== Running the Server ==========
# Save this file as main.py
# Terminal command: uvicorn main:app --reload
# Visit http://127.0.0.1:8000/docs for interactive docs