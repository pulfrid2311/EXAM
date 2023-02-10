from config import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    deliveryAddress = db.Column(db.String(120),nullable=False)
    Contact = db.Column(db.String(120),nullable=False)
    active = db.Column(db.Boolean(120),nullable=False)
    

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    weight = db.Column(db.Float(120),nullable=False)
    description = db.Column(db.String(120),nullable=False)
    
    #def getPriceForQuantity():

    #def getWeight():

class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    qty = db.Column(db.Integer(120),nullable=False)
    taxStatus = db.Column(db.String(120),nullable=False)
    
    #def calculateSubTotal()
    #def calculateWeight()

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    amount = db.Column(db.Float(120),nullable=False)
    Contact = db.Column(db.String(120),nullable=False)
    active = db.Column(db.Boolean(120),nullable=False)
