#!/usr/bin/python3

"""
Test Module for BaseModel Class

This module contains unit tests for the BaseModel class in the AirBnB clone project.
It uses the unittest framework to test various aspects of the BaseModel class.

Classes:
    TestBaseModel: A class containing test cases for the BaseModel class.

Test Cases:
    - test_instance_creation: Tests the creation of a BaseModel instance.
    - test_attribute_initialization: Tests the presence of required attributes in a BaseModel instance.
    - test_str_method: Tests the __str__ method of a BaseModel instance.
    - test_save_method: Tests the save method of a BaseModel instance.
    - test_to_dict_method: Tests the to_dict method of a BaseModel instance.

Usage:
    Run this module directly to execute all the defined tests.
"""

import sys
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
# Adding the project directory to the Python path
sys.path.append('/path/to/your/project')


class TestBaseModelMethods(unittest.TestCase):
    """Test suite to test the Base Model module"""

    @classmethod
    def setUpClass(cls):
        """Setup method for the test class"""
        cls.base_model_instance_1 = BaseModel()
        dictionary = cls.base_model_instance_1.to_dict()
        cls.base_model_instance_2 = BaseModel(**dictionary)
        cls.dictionary_2 = cls.base_model_instance_2.to_dict()
        cls.base_model_instance_3 = BaseModel()
        cls.base_model_instance_3.name = 'assign directly'
        cls.base_model_instance_3.my_number = 90
        cls.base_model_instance_3.id = 20
        cls.dictionary_3 = {
            '__class__': BaseModel, 'name': 'this dictionary', 'number': 98}
        cls.base_model_instance_4 = BaseModel(**cls.dictionary_3)
        cls.dictionary_4 = cls.base_model_instance_4.to_dict()
        cls.base_model_instance_5 = BaseModel(**cls.dictionary_3)

    def test_01_attribute_initialization(self):
        """Test if BaseModel is initialized with the correct types"""
        self.assertIs(type(self.base_model_instance_1.id), str)
        self.assertIs(type(self.base_model_instance_1.created_at), datetime)
        self.assertIs(type(self.base_model_instance_1.updated_at), datetime)

    def test_02_equality_created_new_instances(self):
        """Test equality between newly created instances"""
        self.assertIsNot(self.base_model_instance_1,
                         self.base_model_instance_2)
        self.assertEqual(self.base_model_instance_2.updated_at,
                         self.base_model_instance_1.updated_at)
        self.assertEqual(self.base_model_instance_2.created_at,
                         self.base_model_instance_1.created_at)
        self.assertEqual(self.base_model_instance_2.id,
                         self.base_model_instance_1.id)

    def test_03_equality_created_from_dictionary(self):
        """Test equality between instances created from dictionaries"""
        self.assertEqual(self.base_model_instance_4.name,
                         self.base_model_instance_5.name)
        self.assertEqual(self.base_model_instance_4.number,
                         self.base_model_instance_5.number)

    def test_04_equality_created_directly(self):
        """Test equality for instances created directly"""
        self.assertEqual(self.base_model_instance_3.name, 'assign directly')
        self.assertEqual(self.base_model_instance_3.my_number, 90)
        self.assertEqual(self.base_model_instance_3.id, 20)

    def test_05_kwargs_not_exist(self):
        """Test if attributes not present in kwargs are set"""
        self.assertNotIn('__class__', self.base_model_instance_1.__dict__)
        self.assertNotIn('name', self.base_model_instance_1.__dict__)
        self.assertNotIn('number', self.base_model_instance_1.__dict__)
        self.assertIn('id', self.base_model_instance_1.__dict__)
        self.assertIn('created_at', self.base_model_instance_1.__dict__)
        self.assertIn('updated_at', self.base_model_instance_1.__dict__)

    def test_06_kwargs_exist(self):
        """Test if attributes in kwargs are set"""
        self.assertNotIn('__class__', self.base_model_instance_2.__dict__)
        self.assertNotIn('name', self.base_model_instance_2.__dict__)
        self.assertNotIn('number', self.base_model_instance_2.__dict__)
        self.assertIn('id', self.base_model_instance_2.__dict__)
        self.assertIn('created_at', self.base_model_instance_2.__dict__)
        self.assertIn('updated_at', self.base_model_instance_2.__dict__)

    def test_07_str_method(self):
        """Test str method"""
        expected_str_1 = f"[{self.base_model_instance_1.__class__.__name__}] " \
                         f"({self.base_model_instance_1.id}) {self.base_model_instance_1.__dict__}"
        self.assertEqual(str(self.base_model_instance_1), expected_str_1)

        expected_str_2 = f"[{self.base_model_instance_5.__class__.__name__}] " \
                         f"(20) {self.base_model_instance_5.__dict__}"
        self.assertEqual(str(self.base_model_instance_5), expected_str_2)

    def test_08_save_regular(self):
        """Test save regular"""
        old_updated_at = self.base_model_instance_3.updated_at
        self.base_model_instance_3.name = 'second module'
        self.base_model_instance_3.save()
        self.assertNotEqual(self.base_model_instance_3.created_at,
                            self.base_model_instance_3.updated_at)
        self.assertNotEqual(
            old_updated_at, self.base_model_instance_3.updated_at)

    def test_09_equality_between_equal_instances(self):
        """Test equal instances"""
        base_model_instance_6 = BaseModel()
        base_model_instance_7 = BaseModel()
        self.assertNotEqual(base_model_instance_6, base_model_instance_7)

    def test_10_inequality_between_different_instances(self):
        """Test different instances"""
        dictionary_5 = {
            '__class__': BaseModel, 'name': 'this dictionary', 'number': 98}

        base_model_instance_8 = BaseModel(**dictionary_5)
        base_model_instance_9 = BaseModel(**dictionary_5)

        self.assertNotEqual(base_model_instance_8, base_model_instance_9)

    def test_11_serialization_to_dict(self):
        """Test serialization to dict"""
        self.assertIsInstance(self.base_model_instance_1.to_dict(), dict)

    def test_12_format_datetime(self):
        """Test datetime format"""
        self.assertIs(
            type(self.base_model_instance_1.to_dict()['created_at']), str)
        self.assertIs(
            type(self.base_model_instance_1.to_dict()['updated_at']), str)

    def test_13_deserialization_to_dict(self):
        """Test deserialization to dict"""
        base_model_dict = self.base_model_instance_1.to_dict()
        base_model_instance_2 = BaseModel(**base_model_dict)
        self.assertIsNot(self.base_model_instance_1, base_model_instance_2)

    def test_14_check_type_deserialization(self):
        """Check type in deserialization"""
        self.assertIs(type(self.base_model_instance_1.id), str)
        self.assertIs(type(self.base_model_instance_1.created_at), datetime)


if __name__ == "__main__":
    unittest.main()
