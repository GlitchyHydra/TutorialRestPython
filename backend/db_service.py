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
    #e.g. def insert_patient(name, contacts)
    #name, contacts is the columns of your table(model)
    def insert_patient(name, contacts):
        d

    #TODO GET ALL PATIENTS FROM DB
    def get_patients():
        #TODO IMPLEMENT

    #TODO SELECT PATIENT WHERE name
    def get_patient_by_name(name):
        #TODO IMPLEMENT

    #МОжно сделать еще удаление или еще какие-то методы на свой выбор