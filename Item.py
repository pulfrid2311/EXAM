from config import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    weight = db.Column(db.Float(120),nullable=False)
    description = db.Column(db.String(120),nullable=False)
    
    #def getPriceForQuantity()

    #def getWeight():