from app import db
from flask import request, jsonify
import traceback
from ..models.clients import Clients, ClientsFilterSchema, ClientsSchema, client_schema, clients_schema

'''
Funções de clientes:

- get_clients: retorna todos os clientes
- post_client: cadastra um novo cliente
- client_search: busca clientes com base em filtros
- update_client: atualiza um cliente
- delete_client: deleta um cliente

'''

class ClientController:
    ## GET /client_list
    def get_clients():
        try:
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)
            order_by = request.args.get('order_by', 'id', type=str)
            
            client_query = Clients.query.order_by(order_by)
            total_clients = client_query.count()
            
            clients = client_query.paginate(page=page, per_page=per_page)
            clients_schema = ClientsSchema(many=True)
            result = clients_schema.dump(clients.items)
            
            return jsonify({'message': 'Clientes encontrados!', 'data': result, 'total_clients': total_clients, 'current_page': page, 'per_page': per_page}), 200
        except Exception as e:
            print(e)
            return jsonify({'message': 'Erro ao buscar clientes!', 'data':{}}), 500 

    ## POST /register_client
    ## refatorado
    def post_client():
        try:
            #validando
            data = request.get_json()
            if not all (key in data for key in ('empresarial_name', 'fantasy_name', 'cnpj', 'bairro', 'cep', 'address', 'number', 'city', 'uf', 'email', 'b2b', 'venda_direta', 'revenda')):
                return jsonify({'message': 'Dados incompletos!'}), 400
            
            if Clients.query.filter_by(cnpj=data["cnpj"]).first():
                return jsonify({'message': 'Cliente já cadastrado!'}), 409
            
            #novo cliente
            client = Clients(**data)
            db.session.add(client)
            db.session.commit()
            result = client_schema.dump(client)
            return jsonify({'message': 'Cliente cadastrado com sucesso!', 'data': result}), 201
        except Exception as e:
            traceback.print_exc()
            db.session.rollback() 
            return jsonify({'message': 'Erro ao cadastrar cliente!'}), 500

    def client_search():
        try:
            #carregando e validando os filtros da solicitação
            filters = ClientsFilterSchema().load(request.json)
            query = Clients.query
            
            for key, value in filters.items():
                query = query.filter(getattr(Clients, key) == value)
            
            clients = query.all()
            result = clients_schema.dump(clients)
            
            return jsonify({'message': 'Clientes encontrados!', 'data': result}), 200
        except Exception as e:
            print(e)
            return jsonify({'message': 'Erro ao buscar clientes!', 'data':{}}), 500

    ## PUT /update_client
    def update_client(id: int):
        data = request.get_json()
        if not all (key in data for key in ('empresarial_name', 'fantasy_name', 'cnpj', 'bairro', 'cep', 'address', 'number', 'city', 'uf', 'email', 'b2b', 'venda_direta', 'revenda')):
            return jsonify({'message': 'Dados incompletos!'}), 400
        
        client = Clients.query.get(id)
        if not client:
            return jsonify({'message': 'Cliente não encontrado!'}), 404
        
        
        if not client:
            return jsonify({'message': 'Cliente não encontrado!'}), 404
        
        try:
            client.empresarial_name = data["empresarial_name"]
            client.fantasy_name = data["fantasy_name"]
            client.cnpj = data["cnpj"]
            client.bairro = data["bairro"]
            client.cep = data["cep"]
            client.address = data["address"]
            client.number = data["number"]
            client.city = data["city"]
            client.uf = data["uf"]
            client.email = data["email"]
            client.b2b = data["b2b"]
            client.venda_direta = data["venda_direta"]
            client.revenda = data["revenda"]
            
            db.session.commit()
            result = client_schema.dump(client)
            return jsonify({'message': 'Cliente atualizado com sucesso!', 'data': result}), 200
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'message': 'Erro ao atualizar cliente!', 'data':{}}), 500
        

    ## DELETE /delete_client
    def delete_client(id: int):
        client = Clients.query.get(id)
        if not client:
            return jsonify({'message': 'Cliente não encontrado!'}), 404
        
        try:
            db.session.delete(client)
            db.session.commit()
            
            return jsonify({'message': 'Cliente deletado com sucesso!'}), 200
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'message': 'Erro ao deletar cliente!'}), 500