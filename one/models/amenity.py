#!/usr/bin/python3
"""
Modules creates amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ define amenities that user can choose from to offer at its place"""
    name = ""
