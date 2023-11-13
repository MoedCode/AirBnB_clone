#!/usr/bin/python3
" review class doc"
from models.base_model import BaseModel


class Review(BaseModel):
    """ review class"""
    user_id: str = ""
    place_id: str = ""
    text: str = ""
