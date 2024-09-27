'''Utility classes'''

from sqlalchemy.orm import Session
from . import models, schemas

class Crud:
    def get_item_by_id(db: Session, id: int):
        '''Gets and returns one data item from database for the passed model and id'''

        data = db.query(models.Item).filter(models.Item.id == id).first()
        return data

    def get_items(db: Session):
        '''Gets and returns all data from database for the passed model'''

        data = db.query(models.Item).all()
        return data

    def create_item(db: Session, data: schemas.Item, user_id: int):
        '''Creates a database entry from passed data'''

        item = models.Item(**data.model_dump())
        item.user_id = user_id
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
