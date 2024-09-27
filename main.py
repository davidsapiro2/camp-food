from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas import Item
from .database import SessionLocal, engine
from . import models, schemas
from .utils import Crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)): #optional typing included, this validates and/or convert type

    item = Crud.get_one(db=db, model=models.Item, id=item_id)
    return item

@app.get("/items", response_model=list[schemas.Item])
def read_all_items(db: Session = Depends(get_db)):

    items = Crud.get_all(db=db, model=models.Item)
    return items

### example query parameter ###
@app.get("/items") #localhost:3000/?name=david
def read_item_query(name: str = 'John', num: int | None = None): #optional typing and default included, will validate and/or convert type
    return {"name": name}

@app.post("/items", response_model=schemas.Item)
def create_item(item: schemas.Item, db: Session = Depends(get_db)):
    db_item = Crud.create_one(db=db, model=models.Item, data=item, user_id=1)
    return db_item