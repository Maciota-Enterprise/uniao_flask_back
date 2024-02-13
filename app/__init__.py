from flask import Flask, jsonify, flash, request, redirect
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import mysql.connector

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .models import users, clients
from .routes import routes