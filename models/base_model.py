#!/usr/bin/python3
import uuid


class BaseModel:
    """ Comentario """

    def __init__(self, id, created_at, updated_at):
        """ Comentario """
        self.id = uuid.uuid4()
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """ Comentario """
        print(f"")

