'''Utility classes'''

from sqlalchemy.orm import Session
from . import models, schemas

class Crud:
    def get_one(db: Session, model: models, id: int):
        '''Gets and returns one data item from database for the passed model and id'''

        data = db.query(model).filter(model.id == id).first()
        return data

    def get_all(db: Session, model: models):
        '''Gets and returns all data from database for the passed model'''

        data = db.query(model).all()
        return data

    def create_one(db: Session, model: models, data: schemas, user_id: int):
        '''Creates a database entry from passed data'''

        item = model(**data.dict())
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
