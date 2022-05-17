from flask import Flask
import flask_sqlalchemy
from services.database import db
import os

app = Flask("app")

   #get environment variables from docker-compose.yml
   #db_host = os.environ['DB_HOST']
   #db_name = os.environ['DB_DATABASE']
   #db_user = os.environ['DB_USER']
   #db_pass = os.environ['DB_PASS']
   #db_port = os.environ['DB_PORT']

def create_conn():
   db_host = "localhost"
   db_name = "Patients_db"
   db_user = "postgres"
   db_pass = "5690"
   db_port = "5432"
   return f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

   #propogate to DbService object to create connection SqlAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = create_conn()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = flask_sqlalchemy.SQLAlchemy(app)
#db.init_app(app)