from app import db

class Ward(db.Model):
    __tablename__ = "Wards"

    id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Integer)
    ward_number = db.Column(db.Integer)

    def __repr__(self):
        return f"number: {self.ward_number}, capacity: {self.capacity}"