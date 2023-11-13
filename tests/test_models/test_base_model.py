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
from datetime import datetime
import os


class TestBaseModelMethods(unittest.TestCase):
    """Test suite to test the Base Model module"""

    @classmethod
    def setUpClass(cls):
        """Setup method for the test class"""
        cls.b1 = BaseModel()
        dictionary = cls.b1.to_dict()
        cls.b2 = BaseModel(**dictionary)
        cls.dictionary2 = cls.b2.to_dict()
        cls.b3 = BaseModel()
        cls.b3.name = 'assign directly'
        cls.b3.my_number = 90
        cls.b3.id = 20
        cls.dictionary3 = {
            '__class__': BaseModel, 'name': 'this dictionary', 'number': 98}
        cls.b4 = BaseModel(**cls.dictionary3)
        cls.dictionary4 = cls.b4.to_dict()
        cls.b5 = BaseModel(**cls.dictionary3)

    def test_01_initialize_regular(self):
        """Test if BaseModel is initialized with the correct types"""
        self.assertIs(type(self.b1.id), str)
        self.assertIs(type(self.b1.created_at), datetime)
        self.assertIs(type(self.b1.updated_at), datetime)

    def test_02_equality_created_new_instances(self):
        """Test equality between newly created instances"""
        self.assertIsNot(self.b1, self.b2)
        self.assertEqual(self.b2.updated_at, self.b1.updated_at)
        self.assertEqual(self.b2.created_at, self.b1.created_at)
        self.assertEqual(self.b2.id, self.b1.id)

    def test_03_equality_created_from_dictionary(self):
        """Test equality between instances created from dictionaries"""
        self.assertEqual(self.b4.name, self.b5.name)
        self.assertEqual(self.b4.number, self.b5.number)

    def test_04_equality_created_directly(self):
        """Test equality for instances created directly"""
        self.assertEqual(self.b3.name, 'assign directly')
        self.assertEqual(self.b3.my_number, 90)
        self.assertEqual(self.b3.id, 20)

    def test_05_kwargs_not_exist(self):
        """Test if attributes not present in kwargs are set"""
        self.assertNotIn('__class__', self.b1.__dict__)
        self.assertNotIn('name', self.b1.__dict__)
        self.assertNotIn('number', self.b1.__dict__)
        self.assertIn('id', self.b1.__dict__)
        self.assertIn('created_at', self.b1.__dict__)
        self.assertIn('updated_at', self.b1.__dict__)

    def test_06_kwargs_exist(self):
        """Test if attributes in kwargs are set"""
        self.assertNotIn('__class__', self.b2.__dict__)
        self.assertNotIn('name', self.b2.__dict__)
        self.assertNotIn('number', self.b2.__dict__)
        self.assertIn('id', self.b2.__dict__)
        self.assertIn('created_at', self.b2.__dict__)
        self.assertIn('updated_at', self.b2.__dict__)

    def test_07_str_method(self):
        """Test str method"""
        s = f"[{self.b1.__class__.__name__}] ({self.b1.id}) {self.b1.__dict__}"
        self.assertEqual(str(self.b1), s)
        s2 = f"[{self.b5.__class__.__name__}] (20) {self.b5.__dict__}"
        self.assertEqual(str(self.b5), s2)

    def test_08_save_regular(self):
        """Test save regular"""
        old_updated_at = self.b3.updated_at
        self.b3.name = 'second module'
        self.b3.save()
        self.assertNotEqual(self.b3.created_at, self.b3.updated_at)
        self.assertNotEqual(old_updated_at, self.b3.updated_at)

    def test_09_equality_between_equal_instances(self):
        """Test equal instances"""
        b6 = BaseModel()
        b7 = BaseModel()
        self.assertNotEqual(b6, b7)

    def test_10_inequality_between_different_instances(self):
        """Test different instances"""
        dictionary5 = {
            '__class__': BaseModel, 'name': 'this dictionary', 'number': 98}

        b8 = BaseModel(**dictionary5)
        b9 = BaseModel(**dictionary5)

        self.assertNotEqual(b8, b9)

    def test_11_serialization_to_dict(self):
        """Test serialization to dict"""
        self.assertIsInstance(self.b1.to_dict(), dict)

    def test_12_format_datetime(self):
        """Test datetime format"""
        self.assertIs(type(self.b1.to_dict()['created_at']), str)
        self.assertIs(type(self.b1.to_dict()['updated_at']), str)

    def test_13_deserialization_to_dict(self):
        """Test deserialization to dict"""
        b1_dict = self.b1.to_dict()
        b2 = BaseModel(**b1_dict)
        self.assertIsNot(self.b1, b2)

    def test_14_check_type_deserialization(self):
        """Check type in deserialization"""
        self.assertIs(type(self.b1.id), str)
        self.assertIs(type(self.b1.created_at), datetime)


if __name__ == '__main__':
    """Calling the unit test"""
    unittest.main()
