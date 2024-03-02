from app import db
from app import app
from flask import jsonify
from app.views import users, helper, client
from sqlalchemy import text

# register users
@app.route('/api/v1/signup', methods=['POST'])
def signup():
    return users.signup()

@app.route('/api/v1/auth', methods=['POST'])
def authentication():
    return helper.auth()

@app.route('/api/v1/users/post', methods=['POST'])
def post_user():
    return users.post_user()

@app.route('/api/v1/users/update/<id>', methods=['PUT'])
def put_user(id):
    return users.update_user(id)

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return users.get_users()

@app.route('/api/v1/users/<id>', methods=['GET'])
def get_user(id):
    return users.get_user(id)

#########   clients

@app.route('/api/v1/clients', methods=['GET'])
def get_clients():
    return client.get_clients()

@app.route('/api/v1/client/<id>', methods=['GET'])
def client_by_id(id):
    return client.client_by_id(id)

@app.route('/api/v1/client/update/<id>', methods=['PUT']) 
def update_client(id):
    return client.update_client(id)

@app.route('/api/v1/client/search', methods=['POST'])
def client_search():
    return client.client_search()

@app.route('/api/v1/client/post', methods=['POST'])
# @helper.token_required
def cadastrar_cliente():
    return client.post_client()

@app.route('/api/v1/client/delete/<id>', methods=['DELETE'])
def delete_client(id):
    return client.delete_client(id)



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
