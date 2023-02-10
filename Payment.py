from config import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    amount = db.Column(db.Float(120),nullable=False)
    payment_mode = db.Column(db.String(120),nullable=False)
    __mapper_args__= {'polymorphic_on':payment_mode}
