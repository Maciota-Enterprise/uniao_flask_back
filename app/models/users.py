from datetime import datetime
from app import db, ma

'''definindo classe/tablela dos usuários  e seus campos necessários'''
class Levels(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_levels = db.Column(db.Integer, db.ForeignKey('levels.id'), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    trading_name = db.Column(db.String(20), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    contact = db.Column(db.String(12), nullable=False)
    nickname = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    last_modified = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, id_levels, name, trading_name, cnpj, contact, nickname, password):
        self.id_levels = id_levels
        self.name = name
        self.trading_name = trading_name
        self.cnpj = cnpj
        self.contact = contact
        self.nickname = nickname
        self.password = password

'''definindo o schema do marshmallow para facilitar o uso de json'''
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_levels', 'name', 'trading_name', 'cnpj', 'contact', 'nickname', 'password', 'created_at', 'last_modified')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)  #o parametro many=True é usado quando queremos retornar mais de um registro (Um array)