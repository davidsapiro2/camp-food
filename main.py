from fastapi import FastAPI
from schemas import Item

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

### path parameter ###
@app.get("/items/{item_id}")
def read_item(item_id: int): #optional typing included, this validates and/or convert type
    return {"item_id": item_id}

### query parameter ###
@app.get("/items") #localhost:3000/?name=david
def read_item_query(name: str = 'John', num: int | None = None): #optional typing and default included, will validate and/or convert type
    return {"name": name}

### request body ###
@app.post("/items")
def create_item(item: Item):
    return item