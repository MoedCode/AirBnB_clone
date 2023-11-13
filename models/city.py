#!/usr/bin/python3
"doc"
from models.base_model import BaseModel


class City(BaseModel):
    """city class"""
    name: str = ""
    state_id: str = ""
