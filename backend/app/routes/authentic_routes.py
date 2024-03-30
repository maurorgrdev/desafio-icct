# app/routes/authentic_routes.py

from flask import Blueprint
from flask_restx import fields
from app.controllers import LoginController

def create_authentic_api(api):
    authentic_bp = Blueprint('authentic_bp', __name__)
    
    authentic_ns = api.namespace(name='authentic', description='Operações relacionadas a autenticação')
    login_model = api.model('Login', {
        'login': fields.String(required=True, description='Login do usuário'),
        'senha': fields.String(required=True, description='Senha do usuário')
    })

    # Adicione os recursos com o namespace 
    authentic_ns.add_resource(LoginController, '/login')

    return authentic_bp
