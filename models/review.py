#!/usr/bin/python3
from models.base_model import BaseModel
"""Creates the user's Review class"""


class Review(BaseModel):
    """ Place class
    Public attributes:
        place_id (str): the place id
        user_id (str): the user is
        text (str): the text
    """
    place_id = ""
    user_id = ""
    text = ""
