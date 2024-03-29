# config.py

import os

class Config:
    DEBUG = False
    # Use os.getenv para acessar as variáveis de ambiente do .env
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@teste-icct-db-1/icct'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Outras configurações relevantes aqui

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    # Outras configurações específicas de desenvolvimento aqui

class ProductionConfig(Config):
    # Configurações específicas de produção aqui
    pass
