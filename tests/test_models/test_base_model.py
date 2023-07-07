import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def setUp(self):
        self.base_model = BaseModel()

    def test_id(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_save(self):
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        result = self.base_model.to_dict()
        self.assertIsInstance(result, dict)

    def test_to_dict_contains_correct_values(self):
        result = self.base_model.to_dict()
        self.assertEqual(result['__class__'], 'BaseModel')
        self.assertEqual(result['id'], self.base_model.id)
        self.assertEqual(result['created_at'], self.base_model.created_at.strftime('%Y-%m-%d %H:%M:%S.%f'))
        self.assertEqual(result['updated_at'], self.base_model.updated_at.strftime('%Y-%m-%d %H:%M:%S.%f'))

if __name__ == '__main__':
    unittest.main()

