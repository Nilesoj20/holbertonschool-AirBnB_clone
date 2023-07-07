#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_save(self):
        prev_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(prev_updated_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(type(model_dict), dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in model_dict)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)

    def test_id(self):
        self.assertIsNotNone(self.model.id)
        self.assertEqual(type(self.model.id), str)

    def test_created_at(self):
        self.assertIsNotNone(self.model.created_at)
        self.assertEqual(type(self.model.created_at), datetime)

    def test_str(self):
        model_str = str(self.model)
        self.assertEqual(type(model_str), str)
        self.assertIn(self.model.__class__.__name__, model_str)
        self.assertIn(self.model.id, model_str)
        self.assertIn(str(self.model.__dict__), model_str)


if __name__ == '__main__':
    unittest.main()
