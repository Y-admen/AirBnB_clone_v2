#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        name = ""
        state_id = ""

    def __str__(self):
        """Returns a string representation of the City object"""
        city_dict = self.__dict__.copy()
        if "_sa_instance_state" in city_dict:
            del city_dict["_sa_instance_state"]
        if "name" not in city_dict:
            city_dict["name"] = ""
        return f"[City] ({self.id}) {city_dict}"
