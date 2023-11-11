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
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects
