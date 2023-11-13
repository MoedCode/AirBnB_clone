#!/usr/bin/python3
# main.py
from models.base_model import BaseModel

if __name__ == "__main__":
    my_model = BaseModel()
    print(my_model)

    my_model.save()
    print(my_model)

    my_model_json = my_model.to_dict()
    print(my_model_json)
