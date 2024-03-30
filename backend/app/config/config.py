# app/config/config.py

import os
from app.models import User

class Config:
    DEBUG = False
    # Use os.getenv para acessar as variáveis de ambiente do .env
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@teste-icct-db-1/icct'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração para Flask-JWT
    SECRET_KEY = 'ZJMRzSf3J76J2yiF7znt6n8Xc66ItMOt4DcVaUXoyfw'
    JWT_SECRET_KEY = '2pYWDgRjgVAr22fKjv-VWNovuV0_0T9p5e4F2s1Cdk0'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

def authenticate(username, password):
    # Lógica de autenticação
    pass

def identity(payload):
    user_id = payload['identity']
    # Consulta o banco de dados para encontrar o usuário pelo ID
    return User.query.get(user_id)

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    # Outras configurações específicas de desenvolvimento aqui

class ProductionConfig(Config):
    # Configurações específicas de produção aqui
    pass


# from flask import Flask, Blueprint
# from flask_restx import Api
# from app.controllers import UserController, UserDetailController
# from flask_cors import CORS
# from .database import db  # Supondo que este é o seu objeto de banco de dados

# class Server():
#     def __init__(self):
#         self.app = Flask(__name__)
#         self.blueprint = Blueprint('api', __name__, url_prefix='/api')
#         self.api = Api(self.blueprint, doc='/doc', title='Street Flask API')
#         self.app.register_blueprint(self.blueprint)

#         # Configuração do banco de dados
#         self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@teste-icct-db-1/icct'
#         self.app.config['PROPAGATE_EXCEPTIONS'] = True
#         self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#         # Inicialização do banco de dados
#         db.init_app(self.app)

#         # Adicionando recursos e namespaces
#         self.add_resources_and_namespaces()

#         # Configuração do CORS
#         CORS(self.app, resources={r"/api/*": {"origins": "*"}})

#     def add_resources_and_namespaces(self):
#         user_ns = self.api.namespace(name='User', description='Users related operations')

#         # Adicionar recursos ao namespace do usuário
#         user_ns.add_resource(UserDetailController, '/users/<int:id>')
#         user_ns.add_resource(UserController, '/users')


#     def run(self):
#         self.app.run(
#             port=8000,
#             debug=True,
#             host='0.0.0.0'
#         )

# # Inicializando o servidor
# server = Server()
