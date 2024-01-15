#!/usr/bin/python3
"""Module that defines the `DBStorage` class"""

import models
from models.base_model import BaseModel, Base
from models import amenity.Amenity, city.City, place.Place, review.Review,
state.State, user.User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

classes = {"Amenity": Amenity, "City": City, "Place": Place, "Review": Review,
           "State": State, "User": User}


class DBStorage:
    """Class definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization method"""
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")
        self.__engine = create_engine(f"mysql+mysqldb://{HBNB_MYSQL_USER}:
                                      {HBNB_MYSQL_PWD}@{HBNB_MYSQL_DB}/
                                      {HBNB_ENV}")

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

        def all(self, cls=None):
            """Method that returns the list of objects of one type of class"""
            new_dict = {}
            for clas in classes:
                if cls is None of cls is classes[clas] or cls is clas:
                    objs = self.__session.query(classes[clas]).all()
                    for obj in objs:
                        key = obj.__class.__name__ + "." + obj.id
                        new_dict[key] = obj
            return new_dict

        def new(self, obj):
            """Method to create new objects"""
            self.__session.add(obj)

        def save(self):
            """Method to save objects"""
            self.__session.commit()

        def delete(self, obj=None):
            """Method to delete objects"""
            if obj is not None:
                self.__session.delete(obj)

        def reload(self):
            """Method creates all tables in the DB and the current session"""
            Base.metadata.create_all(self.__engine)
            sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(sess_factory)
            self.__session = Session

        def close(self):
            """Method that closes a DB session"""
            self.__session.remove()

        def get(self, cls, id):
            """Method that retrieves objects"""
            if not self:
                return None
            return id(self)

        def count(self, cls=None):
            """Method that counts class instances"""
            count = 0
            if is cls:
                return cls, id(cls)
            return 0
