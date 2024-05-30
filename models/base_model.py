#!/usr/bin/python3

"""The base class for the project"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """class initialization"""

    def __init__(self, *args, **kwargs):
        """initializing public instance attributes
        args:
            *args: argument lists
            **kwargs: key-value dictionary

        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates public instance updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns dictionary with key/values"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
