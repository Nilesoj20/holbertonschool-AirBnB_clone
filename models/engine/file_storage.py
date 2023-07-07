#!/usr/bin/python3
""" the json file store """

import json
from models.base_model import BaseModel


class FileStorage:
    """Filestore class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary of all objects. """
        return FileStorage.__objects

    def new(self, obj):
        """set a new object in the __objects dictionaty."""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file """
        
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects. """

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
