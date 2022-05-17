from http.client import OK
from flask import render_template,request,redirect,url_for, jsonify
from app import app
from db_service import DbService

db_service = DbService()

#main page after go to website
@app.route('/')
def main():
   patients = db_service.get_patients()
   return render_template('index.html', patients=patients)

'''Get all patients or add new one'''
@app.route('/patients/', methods=['GET', 'POST'])
def patients_req():

   if request.method == 'GET':
      return render_template('create_patient.html')

   data = request.form

   has_fields = ('name' in data) and ('gender' in data) and ('contacts' in data)
   if (has_fields == False):
      return "Not enough data were provided"

   db_service.insert_patient(data['name'], data['gender'], data['contacts'])

   return redirect(url_for('main'))

@app.route('/patients/<int:id>', methods=['POST'])
def patient_by_name(id):
   db_service.delete_patient_by_name(id)
   return redirect(url_for('main'))

@app.route('/accomodation/patients/<name>', methods=['GET'])
def accomodation_by_patient_name(name):
   accomodations = db_service.find_accommodation_by_patient_name(name)

   return render_template('accomodation.html', accomodations=accomodations, search_name=name)

if __name__ == '__main__':
   app.run()