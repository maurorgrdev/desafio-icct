# app/namespaces/user_namespace.py

from flask_restx import Namespace, fields

# Crie o namespace
user_ns = Namespace('User', description='Operações relacionadas a usuário')

# Defina o modelo para o namespace
user_model = user_ns.model('User', {
    'id': fields.Integer(readOnly=True, description='Identificador único do Usuário'),
    # Defina outros campos da User aqui
})

# Defina o esquema para serializar/desserializar objetos User
# user_schema = UserSchema()
