#!/usr/bin/python3
from models.base_model import BaseModel
"""Creates the user's place class"""


class Place(BaseModel):
    """ Place class
    Public attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): name of the amenity
        description (str): description of the place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guests
        price_by_night (int): the price per night
        latitude (float): latitude of the place
        longitude (float): longitude of the place
        amenity_ids (list): list the Amenity
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
