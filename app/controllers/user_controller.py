from flask import request
from flask_restx import Resource
from app.services import UserService
from app.schemas import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserController(Resource):
    def get(self):
        """
        Retorna todos os usuários.
        """
        
        users = UserService.find_all()
        return users_schema.dump(users)

    def post(self):
        """
        Cria um novo usuário.
        """
        data = request.json
        response, status_code = UserService.create(data)
        return response, status_code

class UserDetailController(Resource):
    def get(self, user_id):
        """
        Retorna detalhes de um usuário específico.
        """
        response = UserService.find_by_id(user_id)
        return response

    def put(self, user_id):
        """
        Atualiza os detalhes de um usuário.
        """
        data = request.json
        response = UserService.update(user_id, data)
        return response

    def delete(self, user_id):
        """
        Deleta um usuário.
        """
        response = UserService.delete(user_id)
        return response
