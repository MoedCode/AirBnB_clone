#!/usr/bin/python3
" user module class doc"
from models.base_model import BaseModel


class User(BaseModel):
    """ user module class"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
