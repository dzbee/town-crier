from app import db

class Scenario(db.Model):
    idn = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(), nullable=False)

class Choice(db.Model):
    idn = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())
    scenario_idn = db.Column(db.Integer, db.ForeignKey("scenario.idn"), nullable=False)
    scenario = db.relationship("Scenario", backref="choices", lazy=True, foreign_keys=[scenario_idn])
    target_idn = db.Column(db.Integer, db.ForeignKey("scenario.idn"))
