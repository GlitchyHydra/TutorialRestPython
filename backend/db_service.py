from typing_extensions import Self
from django import db
import flask_sqlalchemy

class DbService:

    db = flask_sqlalchemy.SQLAlchemy()
    IsRunning = False

    '''
    method called when new instance of class will be created
    only single copy of that object can be created
    '''
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DbService, cls).__new__(cls)
        return cls.instance

    #constructor of class
    def __init__(self, app):
        db = flask_sqlalchemy.SQLAlchemy(app)

    #TODO define your methods here
    #e.g. def InsertNewCat(cat)
    #cat is the object of your model
    