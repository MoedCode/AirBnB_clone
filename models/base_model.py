#!/usr/bin/python3
""" doc"""
import uuid
from datetime import datetime
from __init__ import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class."""
        if kwargs:
            self.id = kwargs["id"]
            self.name = kwargs["name"]
            self.my_number = kwargs["my_number"]
            self.created_at: datetime = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )

            self.updated_at: datetime = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )

        else:
            self.id: str = str(uuid.uuid4())
            self.created_at: datetime = datetime.now()
            self.name = None
            self.my_number = None
            self.updated_at: datetime = datetime.now()

            storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Convert the BaseModel instance to a dictionary representation.

        Returns:
        dict: A dictionary containing all keys/values of the instance.
            Includes '__class__', 'created_at', and 'updated_at' keys.
        """
        class_attr = self.__dict__
        filtered_class_attr = dict()

        for key in class_attr:
            if class_attr[key] is not None:
                filtered_class_attr[key] = class_attr[key]
        filtered_class_attr["__class__"] = self.__class__.__name__

        filtered_class_attr["updated_at"]: str = str(self.updated_at.isoformat())
        filtered_class_attr["created_at"]: str = str(self.created_at.isoformat())

        return filtered_class_attr


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print(
            "\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key])
        )

    print("-- my new model :")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
