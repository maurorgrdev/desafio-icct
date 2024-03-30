# app/services/auth_service.py

from flask_jwt_extended import create_access_token
from app.models.user import User

class AuthService:

    @staticmethod
    def authenticate(login, senha):
        # Consulta o banco de dados para encontrar o usuário com o login fornecido
        user = User.query.filter_by(login=login).first()
        
        if not user or not user.check_password(senha):
            return None  # Usuário não encontrado ou senha incorreta
        
        return user

    @staticmethod
    def generate_access_token(user_id):
        # Gera o token JWT para o usuário
        access_token = create_access_token(identity=user_id)
        return access_token
