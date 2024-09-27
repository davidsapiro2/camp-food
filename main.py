from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
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

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)): #optional typing included, this validates and/or convert type

    item = Crud.get_item_by_id(db=db, id=item_id)
    return item

@app.get("/items", response_model=list[schemas.Item])
def read_all_items(db: Session = Depends(get_db)):

    items = Crud.get_items(db=db)
    return items

@app.post("/items", response_model=schemas.Item)
def create_item(item: schemas.Item, db: Session = Depends(get_db)):
    db_item = Crud.create_item(db=db, data=item, user_id=1)
    return db_item