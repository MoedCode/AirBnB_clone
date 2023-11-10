# tests/test_models/test_base_model.py
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_attributes(self):
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_method(self):
        my_model = BaseModel()
        str_representation = str(my_model)
        self.assertIn("[BaseModel] ({})".format(
            my_model.id), str_representation)

    def test_save_method(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)


if __name__ == '__main__':
    unittest.main()
