from werkzeug.security import generate_password_hash
from flask import redirect, flash
from app import db
from flask import request, jsonify
import traceback
from ..models.clients import Clients, user_schema, users_schema

def client_by_cnpj(cnpj):
    try:
        return Clients.query.filter(Clients.cnpj == cnpj).one()
    except Exception as e:
        print(e)
        return None

def post_client():
    empresarial_name = request.json['empresarial_name']
    fantasy_name = request.json['fantasy_name']
    cnpj = request.json['cnpj']
    bairro = request.json['bairro']
    cep = request.json['cep']
    address = request.json['address']
    number = request.json['number']
    city = request.json['city']
    uf = request.json['uf']
    contact = request.json['contact']
    b2b = request.json['b2b']
    venda_direta = request.json['venda_direta']
    revenda = request.json['revenda']
    
    client = Clients(empresarial_name, fantasy_name, cnpj, bairro, cep, address, number, city, uf, contact, b2b, venda_direta, revenda)

    if client_by_cnpj(cnpj):
        flash({'message': 'Cliente já cadastrado!'}), 409
        return redirect('/cadastrar')
    
    try:
        db.session.add(client)
        db.session.commit()
        result = user_schema.dump(client)
        return jsonify({'message': 'Cliente cadastrado com sucesso!', 'data': result}), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({'message': 'Erro ao cadastrar cliente!'}), 500
    
def update_client(id):
    empresarial_name = request.json['empresarial_name']
    fantasy_name = request.json['fantasy_name']
    cnpj = request.json['cnpj']
    bairro = request.json['bairro']
    cep = request.json['cep']
    address = request.json['address']
    number = request.json['number']
    city = request.json['city']
    uf = request.json['uf']
    contact = request.json['contact']
    b2b = request.json['b2b']
    venda_direta = request.json['venda_direta']
    revenda = request.json['revenda']
    
    client = Clients.query.get(id)
    
    if not client:
        return jsonify({'message': 'Cliente não encontrado!'}), 404
    
    try:
        client.empresarial_name = empresarial_name
        client.fantasy_name = fantasy_name
        client.cnpj = cnpj
        client.bairro = bairro
        client.cep = cep
        client.address = address
        client.number = number
        client.city = city
        client.uf = uf
        client.contact = contact
        client.b2b = b2b
        client.venda_direta = venda_direta
        client.revenda = revenda
        db.session.commit()
        result = user_schema.dump(client)
        return jsonify({'message': 'Cliente atualizado com sucesso!', 'data': result}), 200
    except:
        return jsonify({'message': 'Erro ao atualizar cliente!', 'data':{}}), 500
    

def get_clients(empresrial_name):
    try:
        clients = Clients.query.filter(Clients.empresarial_name.like(f'%{empresrial_name}%')).all()
        result = users_schema.dump(clients)
        return jsonify({'message': 'Clientes encontrados!', 'data': result}), 200
    except:
        return jsonify({'message': 'Erro ao buscar clientes!', 'data':{}}), 500