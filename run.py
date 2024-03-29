# run.py

import argparse
from app.app import create_app
import os
from dotenv import load_dotenv  # Importe a função load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Parse dos argumentos de linha de comando
parser = argparse.ArgumentParser(description='Run the Flask application.')
parser.add_argument('--host', default='0.0.0.0', help='Host address to run the application on')  # Adicione um argumento para o host
parser.add_argument('--port', type=int, default=5001, help='Port number to run the application on')
args = parser.parse_args()

# Crie o aplicativo Flask
app = create_app()

# Execute o aplicativo Flask no host e porta especificados
if __name__ == "__main__":
    # Use os.getenv para acessar as variáveis de ambiente do .env
    app.run(host=os.getenv('FLASK_RUN_HOST', '0.0.0.0'), port=os.getenv('FLASK_RUN_PORT', 5001), debug=True)
