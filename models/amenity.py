#!/usr/bin/python3
"  Amenity module class doc"
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity module class"""
    name: str = ""
