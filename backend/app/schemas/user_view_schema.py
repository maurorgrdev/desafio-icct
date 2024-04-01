# app/schemas/user_view_schema

from marshmallow import Schema, fields

class UserViewSchema(Schema):
    id = fields.Integer(dump_only=True)
    nome = fields.String(required=True)
    sobrenome = fields.String(required=True)
    cpf = fields.String(required=True)
    email = fields.Email(required=True)
    login = fields.String(required=True)