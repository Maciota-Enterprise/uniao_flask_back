from app import db
from app import app
from flask import jsonify
from app.views import users
from sqlalchemy import text

@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Hello, World!'})

@app.route('/users', methods=['POST'])
def post_user():
    return users.post_user()

@app.route('/test_database')
def test_database():
    try:
        db.session.query(text("1")).from_statement(text("SELECT 1")).all()
        return jsonify({'message': 'Database is up!'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Database is down!'}), 500
