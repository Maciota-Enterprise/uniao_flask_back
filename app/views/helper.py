from app import app
import jwt
from .users import user_by_email
from werkzeug.security import check_password_hash
from flask import request, jsonify
from functools import wraps
import datetime

def auth():
    email = request.json['email']
    password = request.json['password']
    user = user_by_email(email)
    if not user:
        return jsonify({'message': 'E-mail não encontrado!'}), 401
    
    print(user)
    print(user.password)
    print(check_password_hash(user.password, password))
    if user and check_password_hash(user.password, password):
        token = jwt.encode({'email': user.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}, 
                        app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({'message': 'Validated succesfully','token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})
    
    return jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth = "Login Required"'}), 401

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing', 'data': {}}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = user_by_email(email=data['email'])
        except:
            return jsonify({'message': 'Token is invalid or expired', 'data': {}}), 401
        return f(current_user,*args, **kwargs)
    return decorated