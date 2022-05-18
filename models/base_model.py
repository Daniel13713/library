#!/usr/bin/python3
"""
------------------------------------------------
This module define the base class for all models
for Library Project: Book,User,Loan...
------------------------------------------------
"""

import uuid


class BaseModel:
    """
    ------------------------------------------------
    Base Class for the Models
    ------------------------------------------------
    """

    def __init__(self, *args, **kwargs):
        """
        ------------------------------------------------
        Instatntiates a new model
            - The unique parameter in common is the id
        ------------------------------------------------
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
        else:
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            if not kwargs.get('id'):
                self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        ------------------------------------------------
        Representation in the console (Server side)
        [ClassName] (id) {Values of the object}
        ------------------------------------------------
        """
        ClassName = self.__class__.__name__
        return "[{0}] ({1}) {2}".format(ClassName, self.id, self.__dict__)

    def save(self):
        """
        ------------------------------------------------
        Save the data in the storage: Mysql or files
        ------------------------------------------------
        """
        pass

    def delete(self):
        """
        ------------------------------------------------
        delete the current instance from the storage
        (models.storage) by calling the method delete
        ------------------------------------------------
        """
        pass

