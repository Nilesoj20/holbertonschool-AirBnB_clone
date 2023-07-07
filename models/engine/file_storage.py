#!/usr/bin/python3
""" the json file store """

import json
from models.base_model import BaseModel


class FileStorage:
<<<<<<< HEAD
    """Filestore class """
=======
    """Class that serializes and deserializes 
    instances to a JSON file
    """
>>>>>>> ddf8123afe8b2ad60e2ceb4e925203be8bd34e0c
    __file_path = "file.json"
    __objects = dic()

    def all(self):
<<<<<<< HEAD
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
=======
        """Returns all objects stored in the attribute """
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the dictionary"""
        name_obj = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name_obj, obj.id)] = obj

    def save(self):
        """Saves the objects stored in the dictionary to the JSON file"""
        dict_ = FileStorage.__objects
        obj_dict = {obj: dict_[obj].to_dict() for obj in dict_.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Loads the data from the JSON file and converts it back to objects. """
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(f)
                for val in objdict.values():
                    name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(name)(**val))
>>>>>>> ddf8123afe8b2ad60e2ceb4e925203be8bd34e0c
        except FileNotFoundError:
            pass
