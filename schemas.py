'''Schemas for request body validation'''

from pydantic import BaseModel

### Item models ###

class ItemBase(BaseModel):
    title: str
    description: str
    photo_url: str | None = None

    model_config = {
        "extra": "forbid", # forbids other fields than those declared
        "json_schema_extra": { # example request body for the docs
            "examples" : [
                {
                    "name": "Food",
                    "description": "A very delicious meal",
                    "photo": None
                }
            ]
        }
    }

class Item(ItemBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

### User Models ###

class UserBase(BaseModel):
    name: str
    username: str
    email: str

    model_config = {
        "extra": "forbid", # forbids other fields than those declared
        "json_schema_extra": { # example request body for the docs
            "examples" : [
                {
                    "name": "David",
                    "username": "foodDave",
                    "email": "food@dave.com"
                }
            ]
        }
    }

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    items: list[Item] = []

    class Config:
        orm_mode = True