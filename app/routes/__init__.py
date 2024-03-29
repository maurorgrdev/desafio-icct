# app/routes/__init__.py
from .user_routes import create_user_blueprint

def register_routes(app):
    user_bp = create_user_blueprint()
    app.register_blueprint(user_bp)

    