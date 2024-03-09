from app import db
from flask import request, jsonify
import traceback
from ..models.farm import Farm, FarmFilterSchema, FarmSchema, farm_schema, farms_schema

class FarmController:
    ### GET /farm_list
    def get_farms():
        try:
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)
            order_by = request.args.get('order_by', 'id', type=str)
            
            farm_query = Farm.query.order_by(order_by)
            total_farms = farm_query.count()
            
            farms = farm_query.paginate(page=page, per_page=per_page)
            farms_schema = FarmSchema(many=True)
            result = farms_schema.dump(farms.items)
            
            return jsonify({'farms': result, 'total_farms': total_farms, 'current_page': page, 'per_page': per_page})
        except Exception as e:
            return jsonify({'message': 'Error to get farms', 'error': str(e), 'traceback': traceback.format_exc()}), 500

    ### POST /farm
    def post_farms():
        try:
            data = request.get_json()
            if not all (key in data for key in ("id_Clients", "id_city", "name", "area", "latitude", "longitude", "adress_street", "adress_number", "adress_bairro", "adress_city", "contact")):
                return jsonify({'message': 'Incomplete data!'}), 400
            
            if Farm.query.filter_by(name=data["name"]).first():
                return jsonify({'message': 'Farm already registered!'}), 409
            
            farm = Farm(**data)
            db.session.add(farm)
            db.session.commit()
            result = farm_schema.dump(farm)
            return jsonify({'message': 'Farm registered successfully!', 'data': result}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Error to register farm!', 'error': str(e), 'traceback': traceback.format_exc()}), 500

    def farm_search():
        try:
            filters = FarmFilterSchema().load(request.json)
            query = Farm.query
            
            #lógica de ordenação
            order_by = request.args.get('order_by', 'id', type=str)
            if order_by:
                query = query.order_by(getattr(Farm, order_by))
            
            for key, value in filters.items():
                query = query.filter(getattr(Farm, key) == value)
            
            farms = query.all()
            result = farms_schema.dump(farms)
            
            return jsonify({'message': 'Farms found!', 'data': result}), 200
        except Exception as e:
            return jsonify({'message': 'Error to search farms!', 'error': str(e), 'traceback': traceback.format_exc()}), 500

    ## PUT /update_farm
    def update_farm(id: int):
        data = request.get_json()
        if not all (key in data for key in ("id_Clients", "id_city", "name", "area", "latitude", "longitude", "adress_street", "adress_number", "adress_bairro", "adress_city", "contact")):
            return jsonify({'message': 'Incomplete data!'}), 400
        
        farm = Farm.query.get(id)
        if not farm:
            return jsonify({'message': 'Farm not found!'}), 404
        
        farm.id_Clients = data["id_Clients"]
        farm.id_city = data["id_city"]
        farm.name = data["name"]
        farm.area = data["area"]
        farm.latitude = data["latitude"]
        farm.longitude = data["longitude"]
        farm.adress_street = data["adress_street"]
        farm.adress_number = data["adress_number"]
        farm.adress_bairro = data["adress_bairro"]
        farm.adress_city = data["adress_city"]
        farm.contact = data["contact"]
        
        db.session.commit()
        result = farm_schema.dump(farm)
        return jsonify({'message': 'Farm updated successfully!', 'data': result}), 200