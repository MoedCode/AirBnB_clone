#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """Initialize a new instance of the BaseModel class."""

        self.id: str = str(uuid.uuid4())
        self.created_at: datetime = datetime.now()
        self.name = None
        self.my_number = None
        self.updated_at: datetime = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()

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
