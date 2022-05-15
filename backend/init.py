import imp
from flask import Flask
import os

def init_app():
   app = Flask(__name__)

   #get environment variables from docker-compose.yml
   #db_host = os.environ['DB_HOST']
   #db_name = os.environ['DB_DATABASE']
   #db_user = os.environ['DB_USER']
   #db_pass = os.environ['DB_PASS']
   #db_port = os.environ['DB_PORT']

   db_host = "localhost"
   db_name = "Patients_db"
   db_user = "postgres"
   db_pass = ""
   db_port = "5432"

   #propogate to DbService object to create connection SqlAlchemy
   db_conn = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
   app.config['SQLALCHEMY_DATABASE_URI'] = db_conn
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   app.app_context().push()

   #directory for files from requests
   app.config['UPLOAD_FOLDER'] = os.environ['UPLOAD_FOLDER']

   return app