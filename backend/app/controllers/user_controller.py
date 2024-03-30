from flask import request, jsonify
from flask_restx import Resource, Api
from app.services import UserService
from app.schemas import UserSchema

api = Api()

user_schema = UserSchema()
users_schema = UserSchema(many=True)

user_model = api.model('User', {
    'nome': {'type': 'string', 'required': True, 'description': 'Nome do usuário'},
    'sobrenome': {'type': 'string', 'required': True, 'description': 'Sobrenome do usuário'},
    'cpf': {'type': 'string', 'required': True, 'description': 'CPF do usuário'},
    'email': {'type': 'string', 'required': True, 'description': 'Endereço de e-mail do usuário'},
    'login': {'type': 'string', 'required': True, 'description': 'Login do usuário'},
    'senha': {'type': 'string', 'required': True, 'description': 'Senha do usuário'}
})


class UserController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService() 

    def get(self):
        """
        Retorna todos os usuários.
        """
        users, status_code = self.user_service.find_all()
        return jsonify({'users': users, 'status': status_code})

    @api.expect(user_model)
    def post(self):
        """
        Cria um novo usuário.
        """
        user_data = request.json
        try:
            novo_user, status_code = self.user_service.create(user_data)
            return jsonify({'message': 'Novo usuario criado com sucesso.', 'user': novo_user, 'status': status_code})
        except ValueError as e:
            return {'message': str(e)}, 400


class UserDetailController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService()

    def get(self, id):
        """
        Retorna detalhes de um usuário específico.
        """
        user, status_code = self.user_service.find_by_id(id)
        return jsonify({'user': user, 'status': status_code})

    def put(self, id):
        """
        Atualiza os detalhes de um usuário.
        """
        data = request.json
        user, status_code = self.user_service.update(id, data)
        return jsonify({
            'message': 'Usuário editado com sucesso.',
            'user': user, 
            'status': status_code
        })

    def delete(self, id):
        """
        Deleta um usuário.
        """
        response = self.user_service.delete(id)
        return jsonify(response)
