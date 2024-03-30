# app/schemas/user_schema.py

from marshmallow import Schema, fields, validates, ValidationError
import re

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    nome = fields.String(required=True)
    sobrenome = fields.String(required=True)
    cpf = fields.String(required=True)
    email = fields.Email(required=True)
    login = fields.String(required=True)
    senha_hash = fields.String()

    # @validates('nome')
    # @validates('sobrenome')
    # @validates('login')
    # def validate_only_letters(self, value):
    #     if not value.isalpha():
    #         raise ValidationError("Este campo deve conter apenas letras.")

    # @validates('cpf')
    # def validate_cpf(self, value):
    #     if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
    #         raise ValidationError("CPF inválido.")

    # @validates('email')
    # def validate_email(self, value):
    #     if not re.match(r'^\S+@\S+\.\S+$', value):
    #         raise ValidationError("E-mail inválido.")

    # @validates('senha')
    # def validate_senha(self, value):
    #     # Exemplo de validação de senha: deve ter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas e números
    #     if len(value) < 8 or not any(char.isdigit() for char in value) or not any(char.isupper() for char in value) or not any(char.islower() for char in value):
    #         raise ValidationError("Senha inválida.")
