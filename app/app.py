# app/app.py

from flask import Flask, Blueprint
from flask_restx import Namespace
from app.config.config import Config
from app.config.database import db
from flask_migrate import Migrate
from flask_restx import Api, Resource  # Adicionei a importação de Resource
from .routes import register_routes
from app.controllers import UserController, UserDetailController
from app.namespaces import register_namespaces

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicialização do banco de dados
    with app.app_context():
        db.init_app(app)
        db.create_all()

    # Para registrar as migrações
    migrate = Migrate(app, db) 

    # Configuração do Flask-RESTX
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api = Api(blueprint, version='1.0', title='Minha API Escola',
              description='API para gerenciar informações escolares')
    app.register_blueprint(blueprint)

    # Registrando os namespaces
    register_namespaces(api)

    # Registrando os blueprints
    register_routes(app)

    return app