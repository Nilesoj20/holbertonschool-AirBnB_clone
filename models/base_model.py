#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.
        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        """
        if kwargs:
            # Restore attributes from dictionary representation
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    iso_ = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, iso_))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy
