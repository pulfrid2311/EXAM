import pymysql
from app import app
from config import db
from Cash import Cash 
from check import Check  
from Credit import Credit 
from Item import Item
from OrderDetail import OrderDetail
from OrderStatus import OrderStatus
from Payment import Payment 
from WireTransfer import WireTransfer  

with app.app_context():
    db.create_all()

if(__name__ == '__main__'):
    app.run()
