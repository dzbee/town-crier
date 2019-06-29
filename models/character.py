from app import db

class Character(db.Model):
    idn = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    gender = db.Column(db.Integer, index=True)
    race = db.Column(db.Integer, index=True)
    role = db.Column(db.Integer, index=True)
