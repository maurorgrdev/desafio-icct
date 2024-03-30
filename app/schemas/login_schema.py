from marshmallow import Schema, fields, validate

class LoginSchema(Schema):
    login = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    senha = fields.Str(required=True, validate=validate.Length(min=8))

    # Você pode adicionar mais validações personalizadas, se necessário
