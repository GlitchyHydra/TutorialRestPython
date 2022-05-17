from app import db

class Patient(db.Model):
    __tablename__ = 'Patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(1))
    contacts = db.Column(db.String)

    def __repr__(self):
        return f"name: {self.name}, gender: {self.gender}, contacts: {self.contacts}"

