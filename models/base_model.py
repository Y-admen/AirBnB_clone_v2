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
                        default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

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
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
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
