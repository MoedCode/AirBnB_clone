#!/usr/bin/python3
"doc"
from models.base_model import BaseModel


class Review(BaseModel):
    user_id: str = ""
    place_id: str = ""
    text: str = ""
