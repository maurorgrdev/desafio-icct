from flask import request, jsonify
from flask_restx import Resource, Namespace, Api
from app.models.user import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.schemas import LoginSchema
from app.services import AuthService

api = Api()

login_schema = LoginSchema()

user_model = api.model('User', {
    'login': {'type': 'string', 'required': True, 'description': 'Login do usuário'},
    'senha': {'type': 'string', 'required': True, 'description': 'Senha do usuário'}
})

class LoginController(Resource):
    @api.expect(user_model)
    def post(self):
        # Extrair o login e a senha do corpo da solicitação
        login = request.json.get('login')
        senha = request.json.get('senha')

        # Autenticar o usuário usando o serviço de autenticação
        user = AuthService.authenticate(login, senha)
        if not user:
            return jsonify({'message': 'Credenciais inválidas'}), 401

        # Gerar o token de acesso usando o serviço de autenticação
        access_token = AuthService.generate_access_token(user.id)

        # Retornar o token JWT como resposta
        return jsonify({'access_token': access_token, 'status': 200})
