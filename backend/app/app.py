# app/app.py

from flask import Flask, Blueprint
from flask_restx import Api
from app.config.config import Config, authenticate, identity
from app.config.database import db
from flask_migrate import Migrate
from .routes import register_routes
from flask_jwt_extended import JWTManager
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicialização do banco de dados
    with app.app_context():
        db.init_app(app)
        # db.drop_all()
        db.create_all()

    # Inicialize o JWT
    jwt = JWTManager(app)

    {"origins": "*", }
    # Configuração do CORS
    cors = CORS(app, resources={r"/api/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"], "headers": ["Content-Type", "Authorization"]}})

    # Para registrar as migrações
    migrate = Migrate(app, db) 

    # Configuração do Flask-RESTX
    api_bp = Blueprint('api', __name__, url_prefix='/api')
    api = Api(api_bp, version='1.0', title='Minha API Escola',
              description='API para gerenciar informações escolares')
    app.register_blueprint(api_bp)

    # Registrar os blueprints e as rotas
    register_routes(app, api)

    return app
