#!/usr/bin/python3
"""
Defines city user class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """class that defines city to look for"""
    state_id = ""
    name = ""
