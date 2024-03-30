# app/routes/__init__.py

from .user_routes import create_user_api
from .authentic_routes import create_authentic_api

def register_routes(app, api):
    user_bp = create_user_api(api)
    authentic_bp = create_authentic_api(api)

    app.register_blueprint(user_bp)
    app.register_blueprint(authentic_bp)
