#!/usr/bin/python3
from models.base_model import BaseModel
""" creates the user's city class"""


class City(BaseModel):
    """ city class
    Public attributes:
        state_id (str): state id
        name (str): name of the city
    """
    state_id = ""
    name = ""
