from werkzeug.security import generate_password_hash
from flask import redirect, flash
from app import db
from flask import request, jsonify
import traceback
from ..models.users import Users, user_schema, users_schema

#funções
def user_by_email(email):
    try:
        return Users.query.filter(Users.email == email).one()
    except Exception as e:
        print(e)
        return None

def signup():
    id_levels = request.json['id_levels']
    name = request.json['name']
    trading_name = request.json['trading_name']
    contact = request.json['contact']
    email = request.json['email']
    password = generate_password_hash(request.json['password'])[:100]
    user = Users(id_levels, name, trading_name,  contact, email, password)
    print(len(user.password))

    if user_by_email(email):
        return({'message': 'Usuário já cadastrado!'}), 409
        
    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'Usuário cadastrado com sucesso!', 'data': result}), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({'message': 'Erro ao cadastrar usuário!'}), 500

def update_user(id):
    id_levels = request.json['id_levels']
    name = request.json['name']
    trading_name = request.json['trading_name']
    contact = request.json['contact']
    username = request.json['username']
    password = generate_password_hash(request.json['password'])[:100]
    active = request.json['active']
    
    user = Users.query.get(id)
    
    if not user:
        return jsonify({'message': 'Usuário não encontrado!'}), 404
    pass_hash = generate_password_hash(password)
    
    try:
        user.id_levels = id_levels
        user.name = name
        user.trading_name = trading_name
        user.contact = contact
        user.username = username
        user.password = pass_hash
        user.active = active
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'Usuário atualizado com sucesso!', 'data': result}), 200
    except:
        return jsonify({'message': 'Erro ao atualizar usuário!', 'data':{}}), 500

# def login_user():
#     username = request.json['username']
#     password = request.json['password']
#     user = user_by_username(username)
#     if not user:
#         return jsonify({'message': 'Usuário não encontrado!'}), 404
#     if user and check_password_hash(user.password, password):
#         token = jwt.encode({'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}, 
#                         app.config['SECRET_KEY'], algorithm="HS256")
#         return jsonify({'message': 'Validated succesfully','token': token,
#                         'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})
#     return jsonify({'message': 'Erro ao logar usuário!'}), 500


def get_users():
    all_users =  Users.query.all()
    if all_users:
        result = users_schema.dump(all_users)
        return jsonify({'message':'Successfully fetched', 'data': result})
    
    return jsonify({'message':'No users found', 'data':{}})

def get_user(id):
    user = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({'message':'Successfully fetched', 'data': result}), 201
    
    return jsonify({'message':'No user found', 'data':{}}), 404






# def delete_user(id):
#     user = Users.query.get(id)
#     if not user:
#         return jsonify({'message': 'Usuário não encontrado!'}), 404
    
#     if user:
#         try:
#             db.session.delete(user)
#             db.session.commit()
#             result = user_schema.dump(user)
#             return jsonify({'message': 'Usuário deletado com sucesso!', 'data': result}), 200
#         except Exception as e:
#             print(e)
#             return jsonify({'message': 'Erro ao deletar usuário!', 'data':{}}), 500
        