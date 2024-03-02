from datetime import datetime
from app import db, ma

# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Business_group(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_users = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_group = db.Column(db.Integer, db.ForeignKey('business_group.id'), nullable=False)
    empresarial_name = db.Column(db.String(20), nullable=False)
    fantasy_name = db.Column(db.String(20), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    bairro = db.Column(db.String(20), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    b2b = db.Column(db.Boolean(1), default=True, nullable=False)
    venda_direta = db.Column(db.Boolean(1), default=True, nullable=False)
    revenda = db.Column(db.Boolean(1), default=True, nullable=False)
    active = db.Column(db.Boolean(1), default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    last_modified = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, id_levels, id_group, empresarial_name, fantasy_name, cnpj, bairro, cep, address, number, city, uf, email, b2b, venda_direta, revenda, active = True):
        self.id_levels = id_levels
        self.id_group = id_group
        self.empresarial_name = empresarial_name
        self.fantasy_name = fantasy_name
        self.cnpj = cnpj
        self.bairro = bairro
        self.cep = cep
        self.address = address
        self.number = number
        self.city = city
        self.uf = uf
        self.email = email
        self.b2b = b2b
        self.venda_direta = venda_direta
        self.revenda = revenda
        self.active = active
        
'''definindo o schema do marshmallow para facilitar o uso de json'''
class ClientsFilterSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_levels', 'id_group', 'empresarial_name', 'fantasy_name', 'cnpj', 'bairro', 'cep', 'address', 'number', 'city', 'uf', 'email', 'b2b', 'venda_direta', 'revenda', 'active','created_at', 'last_modified')

class ClientsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_levels', 'id_group', 'empresarial_name', 'fantasy_name', 'cnpj', 'bairro', 'cep', 'address', 'number', 'city', 'uf', 'email', 'b2b', 'venda_direta', 'revenda', 'active', 'created_at', 'last_modified')

client_schema = ClientsSchema()
clients_schema = ClientsSchema(many=True)  #o parametro many=True é usado quando queremos retornar mais de um registro (Um array) 