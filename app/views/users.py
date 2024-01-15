from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
import traceback
from ..models.users import Users, user_schema, users_schema

def post_user():
    id_levels = request.json['id_levels']
    name = request.json['name']
    trading_name = request.json['trading_name']
    cnpj = request.json['cnpj']
    contact = request.json['contact']
    nickname = request.json['nickname']
    password = generate_password_hash(request.json['password'])
    
    user = Users(id_levels, name, trading_name, cnpj, contact, nickname, password)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'Usuário cadastrado com sucesso!', 'data': result}), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({'message': 'Erro ao cadastrar usuário!'}), 500