#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ init constructor method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        f = "%Y-%m-%d %H:%M:%S.%f"
        if len(kwargs) != 0:
            for clave, valor in kwargs.items():
                if clave == "updated_at":
                    self.__dict__[clave] = datetime.strptime(valor, f)
                    continue
                elif clave == "created_at":
                    self.__dict__[clave] = datetime.strptime(valor, f)
                    continue
                else:
                    self.__dict__[clave] = valor
        else:
            models.storage.new(self)

    def __str__(self):
        """ Method __str__ string representation of an object"""
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """ Public instance methods save updates updated_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ dictionary representation with “simple object type” """
        value_class = self.__class__.__name__
        value_update = self.updated_at.strftime('%Y-%m-%d %H:%M:%S.%f')
        value_created = self.created_at.strftime('%Y-%m-%d %H:%M:%S.%f')
        dic = self.__dict__.copy()
        dic["updated_at"] = value_update
        dic["created_at"] = value_created
        dic["__class__"] = value_class
        return dic
