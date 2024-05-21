from datetime import datetime
from app import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Requests(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_client = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    id_farm = db.Column(db.Integer, db.ForeignKey('farm.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    last_modified = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

def __init__(self, id_client, id_farm, id_user, id_product, product_quantity, date, status):
    self.id_client = id_client
    self.id_farm = id_farm
    self.id_user = id_user
    self.id_product = id_product
    self.product_quantity = product_quantity
    self.date = date
    self.status = status

class RequestsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_client', 'id_farm', 'id_user', 'id_product', 'product_quantity', 'date', 'status', 'created_at', 'last_modified')

return_schema = RequestsSchema()
returns_schema = RequestsSchema(many=True)  #o parametro many=True é usado quando queremos retornar mais de um registro (Um array)
