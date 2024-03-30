# app/routes/__init__.py

from .user_routes import create_user_api

def register_routes(app, api):
    user_bp = create_user_api(api)

    app.register_blueprint(user_bp)
