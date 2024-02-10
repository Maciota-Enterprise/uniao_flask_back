from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
import traceback
from ..models.users import Users, user_schema, users_schema

max_password_length = 100

def post_user():
    id_levels = request.json['id_levels']
    name = request.json['name']
    trading_name = request.json['trading_name']
    cnpj = request.json['cnpj']
    contact = request.json['contact']
    username = request.json['username']
    password = generate_password_hash(request.json['password'][:max_password_length])
    
    user = Users(id_levels, name, trading_name, cnpj, contact, username, password)

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
    cnpj = request.json['cnpj']
    contact = request.json['contact']
    username = request.json['username']
    password = generate_password_hash(request.json['password'][:max_password_length])
    active = request.json['active']
    
    user = Users.query.get(id)
    
    if not user:
        return jsonify({'message': 'Usuário não encontrado!'}), 404
    pass_hash = generate_password_hash(password)
    
    try:
        user.id_levels = id_levels
        user.name = name
        user.trading_name = trading_name
        user.cnpj = cnpj
        user.contact = contact
        user.username = username
        user.password = pass_hash
        user.active = active
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'Usuário atualizado com sucesso!', 'data': result}), 200
    except:
        return jsonify({'message': 'Erro ao atualizar usuário!', 'data':{}}), 500


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

def user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()
    except Exception as e:
        print(e)
        return None





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
        