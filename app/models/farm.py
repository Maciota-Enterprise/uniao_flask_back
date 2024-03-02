from datetime import datetime
from app import db, ma

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_clients = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    id_city = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    area = db.Column(db.Float(10), nullable=False)
    adress_street = db.Column(db.String(50), nullable=False)
    adress_number = db.Column(db.String(10), nullable=False)
    adress_bairro = db.Column(db.String(20), nullable=False)
    adress_city = db.Column(db.String(20), nullable=False)
    contact = db.Column(db.String(12), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    last_modified = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    
    def __init__(self, id_clients, id_city, name, area, adress_street, adress_number, adress_bairro, adress_city, contact):
        self.id_clients = id_clients
        self.id_city = id_city
        self.name = name
        self.area = area
        self.adress_street = adress_street
        self.adress_number = adress_number
        self.adress_bairro = adress_bairro
        self.adress_city = adress_city
        self.contact = contact

''' definindo o schema do marshmallow para facilitar o uso de json '''
class FarmFilterSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_clients', 'id_city', 'name', 'area', 'adress_street', 'adress_number', 'adress_bairro', 'adress_city', 'contact', 'created_at', 'last_modified')

class FarmSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_clients', 'id_city', 'name', 'area', 'adress_street', 'adress_number', 'adress_bairro', 'adress_city', 'contact', 'created_at', 'last_modified')

farm_schema = FarmSchema()
farms_schema = FarmSchema(many=True)  #o parametro many=True é usado quando queremos retornar mais de um registro (Um array)
