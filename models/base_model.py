#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """ A base model class that defines all common
    attributes/methods for other classes
    also represents the base model for the Airbnb project
    """
    def __init__(self, *args, **kwargs):
        """ A public instance attribute """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if (len(kwargs) == 0):
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v

    def save(self):
        """ a public instance method that updates the updated_at
        with the currnt date
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """This will print a string representation of the base
        model class for the Airbnb clone project
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
