import unittest
from datetime import datetime
from unittest import mock
from models.tmp_base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_save(self):
        """Test that save method updates 'updated_at'"""
        inst = BaseModel()
        old_updated_at = inst.updated_at
        inst.save()
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id", "created_at", "updated_at", "name", "my_number", "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_self_id(self):
        """Test self.id attribute"""
        inst = BaseModel()
        self.assertIsInstance(inst.id, str)

    def test_self_created_at(self):
        """Test self.created_at attribute"""
        inst = BaseModel()
        self.assertIsInstance(inst.created_at, datetime)

    def test_str(self):
        """Test __str__ method"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

if __name__ == '__main__':
    unittest.main()
