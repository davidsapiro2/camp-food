'''Utility classes'''

from sqlalchemy.orm import Session
import models
import schemas


class Crud:
    def get_one(db: Session, model: models, id: int):
        '''Gets and returns one data item from database for the passed model and id'''

        return db.query(model).filter(model.id == id)

    def get_all(db: Session, model: models):
        '''Gets and returns all data from database for the passed model'''

        return db.query(model).all()
