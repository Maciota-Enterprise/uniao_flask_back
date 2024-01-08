import datetime
from app import db, ma


'''definindo classe/tablela dos usuários  e seus campos necessários'''

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

def __init__(self, username, password, name, email):
    self.username = username
    self.password = password
    self.name = name
    self.email = email

'''definindo o schema do marshmallow para facilitar o uso de json'''
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'name', 'email', 'created_at')

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)  #o parametro many=True é usado quando queremos retornar mais de um registro (Um array)