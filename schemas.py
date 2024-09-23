'''Schemas for request body validation'''

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    photo: str | None = None

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
