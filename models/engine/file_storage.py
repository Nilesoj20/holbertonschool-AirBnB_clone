#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """Comentario """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Comentario """
        return FileStorage.__objects

    def new(self, obj):
        """Comentario """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Comentario """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Comentario """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
