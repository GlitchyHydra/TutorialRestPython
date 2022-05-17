
from app import db

from models import *

class DbService:

    def insert_patient(self, name, gender, contacts): 
        '''Insert one patient in DB'''

        new_patient = Patient(name=name, gender=gender, contacts=contacts)
        db.session.add(new_patient)
        db.session.commit()
        return {"message": f"patient {new_patient.name} has been added successfully."}

    #GET ALL PATIENTS FROM DB
    def get_patients(self):
        #class 'flask_sqlalchemy.model.DefaultMeta'
        #<class 'module'>
        a = type(Patient)
        patients = Patient.query.all()# Patient.query.all()
        results = [
            {
                "name": patient.name,
                "gender": patient.gender,
                "contacts": patient.contacts
            } for patient in patients]

        return patients#{"Count": len(results), "Patients in Hospital": results}

    #SELECT PATIENT WHERE name
    def get_patient_by_name(self, name):
        patient = Patient.query.get_or_404(name)
        return patient if patient else f"No patients with name: {name}"
        
    #Delete patient by id
    def delete_patient_by_name(self, id):
        patient = Patient.query.get_or_404(id)
        if patient:
            db.session.delete(patient)
            db.session.commit()
            return {"message": f"Patient {patient.name} successfully deleted."}
        else: 
            return False
    
    #find accomadation by patient name
    #INNER JOIN BY FK
    def find_accommodation_by_patient_name(self,name):
        return Accommodation.query.join(Patient).filter_by(name=name)
