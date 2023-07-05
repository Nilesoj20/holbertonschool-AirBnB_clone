#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    """ Comentario """

    def __init__(self, created_at, updated_at):
        """ Comentario """
        self.id = uuid.uuid4()
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """ Comentario """
        print(f"[{__class__.__name__}] (self.id) self.__dict__")

    def save(self):
        """ Comentario """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Comentario """
        return {'}

