# app/namespaces/__init__.py

from app.controllers import UserController, UserDetailController

def register_namespaces(api):

    user_ns = api.namespace(name='User', description='Operações relacionadas a usuário')
    user_ns.add_resource(UserController, '/users')
    user_ns.add_resource(UserDetailController, '/users/<int:id>')