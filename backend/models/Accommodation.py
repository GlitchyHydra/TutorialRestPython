from sqlalchemy.orm import backref
from app import db

class Accommodation(db.Model):
    __tablename__ = "Accommodation"

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("Patients.id"))
    ward_id = db.Column(db.Integer, db.ForeignKey("Wards.id"))
    date = db.Column(db.DATE)
    patient = db.relationship("Patient", backref=backref("accommodation", lazy="dynamic"))
    ward = db.relationship("Ward", backref=backref("accommodation", lazy="dynamic"))

    def __repr__(self):
        return f"Accomodation:\n id: {id}, date: {date}\nPatient name: {patient.name},  Ward number: {ward.number}"