from app import db
from flask import request, jsonify
import traceback
from ..models.farm import Farm, FarmFilterSchema, FarmSchema, farm_schema, farms_schema


### GET /farm_list
def get_farms():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        farm_query = Farm.query
        total_farms = farm_query.count()
        
        farms = farm_query.paginate(page=page, per_page=per_page)
        farms_schema = FarmSchema(many=True)
        result = farms_schema.dump(farms.items)
        
        return jsonify({'farms': result, 'total_farms': total_farms, 'current_page': page, 'per_page': per_page})
    except Exception as e:
        return jsonify({'message': 'Error to get farms', 'error': str(e), 'traceback': traceback.format_exc()}), 500

### POST /farm


