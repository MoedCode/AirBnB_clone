#!/usr/bin/python3

"""
BaseModel Class for AirBnB Clone Project

This module defines the BaseModel class for the AirBnB clone project. The BaseModel class
serves as the parent class for other classes, providing common attributes and methods.

Classes:
    BaseModel: A class representing the base model for other classes in the project.

Attributes:
    - id (str): A unique identifier generated using the uuid module.
    - created_at (datetime): The datetime when an instance is created.
    - updated_at (datetime): The datetime when an instance is created and updated.

Methods:
    - __init__: Initializes a new instance of the BaseModel class.
    - __str__: Returns a string representation of the BaseModel instance.
    - save: Updates the 'updated_at' attribute with the current datetime.
    - to_dict: Converts the BaseModel instance to a dictionary representation.

Usage:
    This module can be used standalone to create an instance of BaseModel and print its dictionary representation.
"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """Initialize a new instance of the BaseModel class."""
        self.id = str(uuid.uuid4())  # Generate a unique ID
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict


if __name__ == "__main__":
    # Create an instance of BaseModel and print its dictionary representation
    bm = BaseModel().to_dict()
    print(bm)
