#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class definition"""
    if models.storage_t == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationshp("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialization method"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """Method that gets list of city instances related to state"""
            list_city =[]
            cities = models.storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
