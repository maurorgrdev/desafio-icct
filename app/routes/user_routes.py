# app/routes/user_routes.py

from flask import Blueprint
from flask_restx import Api, Resource
from app.controllers import UserController, UserDetailController

def create_user_blueprint():
    user_bp = Blueprint('user_bp', __name__)
    api = Api(user_bp)
    
    api.add_resource(UserController, '/user')
    api.add_resource(UserDetailController, '/user/<int:id>')
    
    return user_bp
