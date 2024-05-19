#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Represents a state in the HBNB project.
    """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
        name = Column(String(128), nullable=False)
    else:
        name = ""

    @property
    def cities(self):
        """ Returns list of cities according to state.id"""
        from models import storage
        from models.city import City
        cities = []
        all_cities = storage.all(City).values()
        for obj in all_cities:
            if isinstance(obj, City) and obj.state_id == self.id:
                cities.append(obj)
        return cities
