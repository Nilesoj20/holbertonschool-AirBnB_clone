#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    """defines all common attributes/methods for other classes """

    def __init__(self):
        """ init constructor method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Method __str__ string representation of an object"""
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """ Public instance methods save updates updated_at """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ dictionary representation with “simple object type” """
        value_class = self.__class__.__name__
        value_update = self.updated_at.isoformat()
        value_created = self.created_at.isoformat()
        dic = dict()
        for clave, value in self.__dict__.items():
            dic[clave] = value
            dic['update_at'] = value_update
            dic['created_at'] = value_created
            dic['__class__'] = value_class
        return dic
