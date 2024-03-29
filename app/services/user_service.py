from app.config.database import db
from app.models import User
from app.schemas import UserSchema
from marshmallow import ValidationError

user_schema = UserSchema()

class UserService:
    @staticmethod
    def create(data):
        try:
            novo_usuario = user_schema.load(data)
            db.session.add(novo_usuario)
            db.session.commit()
            return user_schema.dump(novo_usuario), 201
        except ValidationError as e:
            db.session.rollback()
            return {'message': 'Erro ao criar usuário', 'errors': e.messages}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': 'Erro ao criar usuário', 'error': str(e)}, 500

    @staticmethod
    def find_by_id(user_id):
        user = User.query.get(user_id)
        if user:
            return user_schema.dump(user)
        else:
            return {'message': 'Usuário não encontrado'}, 404

    @staticmethod
    def find_all():
        users = User.query.all()
        return user_schema.dump(users)

    @staticmethod
    def update(user_id, data):
        try:
            usuario_atualizado = User.query.get(user_id)
            if usuario_atualizado:
                user_data = user_schema.load(data)
                for key, value in user_data.items():
                    setattr(usuario_atualizado, key, value)
                db.session.commit()
                return user_schema.dump(usuario_atualizado)
            else:
                return {'message': 'Usuário não encontrado'}, 404
        except ValidationError as e:
            db.session.rollback()
            return {'message': 'Erro ao atualizar usuário', 'errors': e.messages}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': 'Erro ao atualizar usuário', 'error': str(e)}, 500

    @staticmethod
    def delete(user_id):
        try:
            usuario = User.query.get(user_id)
            if usuario:
                db.session.delete(usuario)
                db.session.commit()
                return {'message': 'Usuário deletado com sucesso'}
            else:
                return {'message': 'Usuário não encontrado'}, 404
        except Exception as e:
            db.session.rollback()
            return {'message': 'Erro ao deletar usuário', 'error': str(e)}, 500
