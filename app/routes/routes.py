from app import db
from app import app
from flask import jsonify
from app.views import users, helper, client, farm
from app.views.client import ClientController
from app.views.farm import FarmController
from app.views.users import Users, UserController
from sqlalchemy import text

# register users
@app.route('/api/v1/signup', methods=['POST'])
def signup():
    return Users.signup()

@app.route('/api/v1/auth', methods=['POST'])
def authentication():
    return helper.auth()

@app.route('/api/v1/users/post', methods=['POST'])
def post_user():
    return users.post_user()

@app.route('/api/v1/users/update/<id>', methods=['PUT'])
def put_user(id):
    return UserController.update_user(id)

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return UserController.get_users()

@app.route('/api/v1/users/<id>', methods=['GET'])
def get_user(id):
    return UserController.get_user(id)

#########   clients

@app.route('/api/v1/clients', methods=['GET'])
def get_clients():
    return ClientController.get_clients()

@app.route('/api/v1/client/<id>', methods=['GET'])
def client_by_id(id):
    return ClientController.client_by_id(id)

@app.route('/api/v1/client/update/<id>', methods=['PUT']) 
def update_client(id):
    return ClientController.update_client(id)

@app.route('/api/v1/client/search', methods=['POST'])
def client_search():
    return ClientController.client_search()

@app.route('/api/v1/client/post', methods=['POST'])
# @helper.token_required
def cadastrar_cliente():
    return ClientController.post_client()

@app.route('/api/v1/client/delete/<id>', methods=['DELETE'])
def delete_client(id):
    return ClientController.delete_client(id)

#########   farms
@app.route('/api/v1/farms', methods=['GET'])
def get_farms():
    return FarmController.get_farms()

@app.route('/api/v1/farm/post', methods=['POST'])
def post_farms():
    return FarmController.post_farms()

@app.route('/api/v1/farm/update/<id>', methods=['PUT'])
def put_farm(id):
    return FarmController.update_farm(id)

@app.route('/api/v1/farm/search', methods=['POST'])
def farm_search():
    return FarmController.farm_search()

@app.route('/api/v1/farm/delete/<id>', methods=['DELETE'])
def delete_farm(id):
    return FarmController.delete_farm(id)

############################################################################################################
#teste do banco de dados
@app.route('/test_database')
def test_database():
    try:
        db.session.query(text("1")).from_statement(text("SELECT 1")).all()
        return jsonify({'message': 'Database is up!'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Database is down!'}), 500
############################################################################################################
