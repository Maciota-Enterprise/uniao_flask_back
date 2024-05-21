from app import db
from flask import request, jsonify
import traceback
from ..models.requests import Requests, RequestsSchema, request_schema, requests_schema


class RequestController:
    ### GET /requests   
    def get_requests():
        try:
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)
            order_by = request.args.get('order_by', 'id', type=str)
            
            request_query = Requests.query.order_by(order_by)
            total_requests = request_query.count()
            
            requests = request_query.paginate(page=page, per_page=per_page)
            requests_schema = RequestsSchema(many=True)
            result = requests_schema.dump(requests.items)
            
            return jsonify({'requests': result, 'total_requests': total_requests, 'current_page': page, 'per_page': per_page})
        except Exception as e:
            return jsonify({'message': 'Error to get requests', 'error': str(e), 'traceback': traceback.format_exc()}), 500
    ### POST /requests
    def post_request():
        try:
            id_client = request.json['id_client']
            id_farm = request.json['id_farm']
            id_user = request.json['id_user']
            id_product = request.json['id_product']
            product_quantity = request.json['product_quantity']
            date = request.json['date']
            status = request.json['status']
            
            new_request = Requests(id_client, id_farm, id_user, id_product, product_quantity, date, status)
            db.session.add(new_request)
            db.session.commit()
            
            return request_schema.jsonify(new_request)
        except Exception as e:
            return jsonify({'message': 'Error to create request', 'error': str(e), 'traceback': traceback.format_exc()}), 500
    
    def search_request():
        try:
            id_client = request.args.get('id_client')
            id_farm = request.args.get('id_farm')
            id_user = request.args.get('id_user')
            id_product = request.args.get('id_product')
            product_quantity = request.args.get('product_quantity')
            date = request.args.get('date')
            status = request.args.get('status')
            
            request_query = Requests.query.filter_by(id_client=id_client, id_farm=id_farm, id_user=id_user, id_product=id_product, product_quantity=product_quantity, date=date, status=status)
            total_requests = request_query.count()
            
            requests = request_query.all()
            requests_schema = RequestsSchema(many=True)
            result = requests_schema.dump(requests)
            
            return jsonify({'requests': result, 'total_requests': total_requests})
        except Exception as e:
            return jsonify({'message': 'Error to search request', 'error': str(e), 'traceback': traceback.format_exc()}), 500
    
    # PUT /update_request/<id>
    def update_request(id: int):
        data = request.get_json()
        if not all (key in data for key in ('id_client', 'id_farm', 'id_user', 'id_product', 'product_quantity', 'date', 'status')):
            return jsonify({'message': 'Dados incompletos!'}), 400
        
        request = Requests.query.get(id)
        if not request:
            return jsonify({'message': 'Request not found!'}), 404
        try:
            request = Requests.query.get(id)
            request.id_client = request.json['id_client']
            request.id_farm = request.json['id_farm']
            request.id_user = request.json['id_user']
            request.id_product = request.json['id_product']
            request.product_quantity = request.json['product_quantity']
            request.date = request.json['date']
            request.status = request.json['status']
            
            db.session.commit()
            result = request_schema.dump(request)
            return jsonify({'message': 'Pedido atualizado com sucesso!', 'data': result}), 200
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'message': 'Erro ao atualizar pedido!', 'data':{}}), 500

    #DELETE /requests/<id>
    def delete_request(id: int):
        try:
            request = Requests.query.get(id)
            db.session.delete(request)
            db.session.commit()
            return request_schema.jsonify(request)
        except Exception as e:
            return jsonify({'message': 'Error to delete request', 'error': str(e), 'traceback': traceback.format_exc()}), 500
        