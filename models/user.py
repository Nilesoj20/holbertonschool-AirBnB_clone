#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """User Class that inherits
    Args:
        email (str): user's email
        password (str): user's password
        first_name (str): user's first name
        last_name (str): user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
