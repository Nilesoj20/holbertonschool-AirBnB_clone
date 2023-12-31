#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Class that serializes and deserializes
    instances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects stored in the attribute """
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the dictionary"""
        name_obj = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name_obj, obj.id)] = obj

    def save(self):
        """Saves the objects stored in the dictionary to the JSON file"""
        dict_ = FileStorage.__objects
        obj_dict = {key: dict_[key].to_dict() for key in dict_.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Loads the data from the JSON file and
        converts it back to objects
        """
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for val in obj_dict.values():
                    name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(name)(**val))
        except FileNotFoundError:
            return
