#!/usr/bin/python3

"""
Test Module for BaseModel Class

This module contains unit tests for the BaseModel class in the AirBnB clone project.
It uses the unittest framework to test various aspects of the BaseModel class.

Classes:
    TestBaseModel: A class containing test cases for the BaseModel class.

Test Cases:
    - test_instance_creation: Tests the creation of a BaseModel instance.
    - test_attributes: Tests the presence of required attributes in a BaseModel instance.
    - test_str_method: Tests the __str__ method of a BaseModel instance.
    - test_save_method: Tests the save method of a BaseModel instance.
    - test_to_dict_method: Tests the to_dict method of a BaseModel instance.

Usage:
    Run this module directly to execute all the defined tests.
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        """Test the creation of a BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_attributes(self):
        """Test the presence of required attributes in a BaseModel instance."""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_str_method(self):
        """Test the __str__ method of a BaseModel instance."""
        my_model = BaseModel()
        str_representation = str(my_model)
        self.assertIn("[BaseModel] ({})".format(my_model.id), str_representation)

    def test_save_method(self):
        """Test the save method of a BaseModel instance."""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of a BaseModel instance."""
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)


if __name__ == "__main__":
    unittest.main()
