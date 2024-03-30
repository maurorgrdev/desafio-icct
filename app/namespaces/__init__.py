# app/namespaces/__init__.py

# from flask_restx import fields
# from app.controllers import UserController, UserDetailController

# def register_namespaces(api):
#     user_ns = api.namespace(name='User', description='Operações relacionadas a usuário')
#     user_model = api.model('User', {
#         'nome': fields.String(required=True, description='Nome do usuário'),
#         'sobrenome': fields.String(required=True, description='Sobrenome do usuário'),
#         'cpf': fields.String(required=True, description='CPF do usuário'),
#         'email': fields.String(required=True, description='Endereço de e-mail do usuário'),
#         'login': fields.String(required=True, description='Login do usuário'),
#         'senha': fields.String(required=True, description='Senha do usuário')
#     })

#     user_ns.add_resource(UserController, '/user', resource_class_kwargs={'user_ns': user_ns})
#     user_ns.add_resource(UserDetailController, '/user/<int:id>')
