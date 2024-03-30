# app/routes/user_routes.py

from flask import Blueprint
from flask_restx import fields
from app.controllers import UserController, UserDetailController

def create_user_api(api):
    user_bp = Blueprint('user_bp', __name__)
    
    user_ns = api.namespace(name='user', description='Operações relacionadas a usuário')
    user_model = api.model('User', {
        'nome': fields.String(required=True, description='Nome do usuário'),
        'sobrenome': fields.String(required=True, description='Sobrenome do usuário'),
        'cpf': fields.String(required=True, description='CPF do usuário'),
        'email': fields.String(required=True, description='Endereço de e-mail do usuário'),
        'login': fields.String(required=True, description='Login do usuário'),
        'senha': fields.String(required=True, description='Senha do usuário')
    })

    # Adicione os recursos com o namespace user_ns
    user_ns.add_resource(UserController, '/', resource_class_kwargs={'user_ns': user_ns})
    user_ns.add_resource(UserDetailController, '/<int:id>', resource_class_kwargs={'user_ns': user_ns})

    return user_bp
