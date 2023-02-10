from config import db

class Cash(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    cashTendered = db.Column(db.Float(120),nullable=False)
    __mapper_args__= {'polymorphic_identity:"Cash"'} 