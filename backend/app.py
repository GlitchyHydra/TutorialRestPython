from http.client import OK
from flask import Flask,abort,render_template,request,redirect,url_for, jsonify
import os
from backend.models.Patient import Patient

import init
from db_service import DbService

app = init.init_app()
db_service = DbService(app)

@app.route('/query')
def query():
   surname = request.args.get('surname')

   return '''<h1>The surname value is: {}</h1>'''.format(surname)

#TODO EXAMPLE OF HOW TO CALL VIOLETTA's methods from db_service class
#And parse data from json
@app.route('/patients', methods=['GET', 'POST'])
def patients_request():
   if request.method =='POST':
      body_data = request.json
      patient_name = body_data['name']
      patient_cont = body_data['contacts']
      #insert patient
      db_service.insert_patient(patient_name, patient_cont)
      
      return OK("inserted")
   else:
      body_data = request.json

      #EXAMPLE как сделать условие по возвращению всех 
      #пациентов или только одного, если ключ name присутствует
      if 'name' not in body_data:
         return jsonify(db_service.get_cats())

      return jsonify(db_service.get_patient(body_data['name']))

@app.route('/success/<name>')
def success(name):
   return 'welcome, %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))




@app.route('/upload/',methods = ['GET','POST'])
def upload_file():
   if request.method =='POST':
      file = request.files['file[]']
      if file:
         filename = file.filename
         file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
         return "The file is uploaded"
   return render_template('upload.html')


if __name__ == '__main__':
   app.run()