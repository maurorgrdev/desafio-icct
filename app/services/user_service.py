from app.config.database import db
from app.models import User
from app.schemas import UserSchema
from marshmallow import ValidationError
from flask import jsonify

def handle_database_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            db.session.rollback()
            return {'message': 'Erro de validação', 'errors': e.messages}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': 'Erro interno do servidor', 'error': str(e)}, 500
    return wrapper

class UserService:
    def __init__(self):
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)

    @handle_database_errors
    def create(self, data):
        # Desserializar os dados usando o schema do usuário
        senha = data.pop('senha', None)

        # Desserialize os dados usando o schema do usuário
        novo_usuario_data = self.user_schema.load(data)
        
        # Criar uma nova instância de User com os dados do esquema
        novo_usuario = User(**novo_usuario_data)

        # Configurar a senha usando o método set_password
        novo_usuario.set_password(senha)

        # Adicionar o novo usuário ao banco de dados
        db.session.add(novo_usuario)
        db.session.commit()

        return self.user_schema.dump(novo_usuario), 201

    @handle_database_errors
    def find_by_id(self, id):
        user = User.query.get(id)
        if user:
            return self.user_schema.dump(user), 200
        else:
            return {'message': 'Usuário não encontrado'}, 404

    @handle_database_errors
    def find_all(self):
        users = User.query.all()
        return self.users_schema.dump(users, many=True), 200


    @handle_database_errors
    def update(self, id, data):
        try:
            # Buscar o usuário pelo ID
            user = User.query.get(id)
            if not user:
                return {'message': 'Usuário não encontrado'}, 404

            # Atualizar os campos do usuário com os novos dados
            for key, value in data.items():
                setattr(user, key, value)

            # Salvar as alterações no banco de dados
            db.session.commit()

            # Serializar o usuário atualizado
            user_serialized = self.user_schema.dump(user)

            # Retornar os dados do usuário atualizado
            return  user_serialized, 200
        except Exception as e:
            # Em caso de erro, retornar uma resposta de erro interno do servidor
            return {'message': 'Erro interno do servidor', 'error': str(e)}, 500

    @handle_database_errors
    def delete(self, id):
        usuario = User.query.get(id)
        if not usuario:
            return {'message': 'Usuário não encontrado'}, 404
        db.session.delete(usuario)
        db.session.commit()
        return {'message': 'Usuário deletado com sucesso'}
