"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "users"

    first_name = db.Column(db.String(300), primary_key=True)
    last_name = db.Column(db.String(300), primary_key=True)

    def __init__(self, first_name, last_name, age=None):
        """ Create a new User """
        self.first_name = first_name
        self.last_name = last_name