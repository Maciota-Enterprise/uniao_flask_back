from app import app
import jwt
from .users import user_by_username
from werkzeug.security import check_password_hash
from flask import request, jsonify
from functools import wraps
import datetime

def auth():
    auth_data = request.authorization
    if not auth_data or not auth_data.username or not auth_data.password:
        return jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    user = user_by_username(auth_data.username)
    if not user:
        return jsonify({'message': 'User not found', 'data': {}}), 404

    if user and check_password_hash(user.password, auth_data.password):
        token = jwt.encode({'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) }, 
                        app.config['SECRET_KEY'])
        return jsonify({'message': 'Validated succesfully','token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})
        
    return jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing', 'data': {}}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = user_by_username(username=data['username'])
        except:
            return jsonify({'message': 'Token is invalid or expired', 'data': {}}), 401
        return f(current_user,*args, **kwargs)
    return decorated