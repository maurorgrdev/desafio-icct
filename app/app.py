from flask import Flask
from app.config.config import Config
from app.config.database import db
from flask_migrate import Migrate
from flask_restx import Api, Resource  # Adicionei a importação de Resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicialização do banco de dados
    with app.app_context():
        db.init_app(app)
        db.create_all()

    # Configuração do Flask-RESTX
    api = Api(app, version='1.0', title='Minha API Escola',
              description='API para gerenciar informações escolares')

    # Definindo uma namespace para a API
    # namespace = api.namespace('hello', description='Hello World operations')



    return app
