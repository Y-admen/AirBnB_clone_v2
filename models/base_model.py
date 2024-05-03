#!/usr/bin/python3
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
import uuid

Base = declarative_base()


class BaseModel:
    """
    Base class for all models.
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.utc)
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utc)

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """
        Save the instance to the database.
        """
        self.updated_at = datetime.now(timezone.utc)
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance.
        """
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.datetime.utcnow()
        result["updated_at"] = self.updated_at.datetime.utcnow()
        if "_sa_instance_state" in result:
            del result["_sa_instance_state"]
        return result

    def delete(self):
        """
        Delete the instance from the database.
        """
        from models import storage
        storage.delete(self)

    def __str__(self):
        """print representation"""
        d = self.__dict__.copy()  # create a copy of the dictionary
        cls = self.__class__.__name__
        if "_sa_instance_state" in d:
            del d["_sa_instance_state"]
        return f"[{cls}] ({self.id}) {d}"
