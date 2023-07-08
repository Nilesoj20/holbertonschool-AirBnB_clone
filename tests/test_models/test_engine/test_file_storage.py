import unittest
from models.base_model import BaseModel
from models.user import User
from file_storage import FileStorage
import os


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_file_path(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all(self):
        obj = User()
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {"User.{}".format(obj.id): obj})

    def test_new(self):
        obj = User()
        self.storage.new(obj)
        self.assertEqual(self.storage._FileStorage__objects, {"User.{}".format(obj.id): obj})

    def test_save(self):
        obj = User()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        obj = User()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertEqual(all_objects, {"User.{}".format(obj.id): obj})


if __name__ == '__main__':
    unittest.main()

