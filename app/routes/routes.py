from app import db
from app import app
from flask import jsonify
from app.views import users, helper, client
from sqlalchemy import text


@app.route('/signup', methods=['POST'])
def signup():
    return users.signup()

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    return client.post_client()

############################################################################################################
#teste da api
@app.route('/', methods=['GET'])
@helper.token_required
def root(current_user):
    return jsonify({'message': 'Hello, World!'})

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

@app.route('/users', methods=['POST'])
def post_user():
    return users.post_user()

@app.route('/users/<id>', methods=['PUT'])
def put_user(id):
    return users.update_user(id)

@app.route('/users', methods=['GET'])
def get_users():
    return users.get_users()

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    return users.get_user(id)

@app.route('/auth', methods=['POST'])
def authentication():
    return helper.auth()

# @app.route('/users/<id>', methods=['DELETE'])
# def delete_user(id):
#     return users.delete_user(id)


