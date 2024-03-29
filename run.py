import argparse
from app.app import create_app
import os
import time  # Importe o módulo time

from dotenv import load_dotenv

# Carregue as variáveis de ambiente do arquivo .env
load_dotenv()

# Parse dos argumentos de linha de comando
parser = argparse.ArgumentParser(description='Run the Flask application.')
parser.add_argument('--host', default='0.0.0.0', help='Host address to run the application on')
parser.add_argument('--port', type=int, default=5001, help='Port number to run the application on')
args = parser.parse_args()

# Crie o aplicativo Flask
app = None

# Tente criar o aplicativo Flask várias vezes até que a conexão com o banco de dados seja estabelecida
for attempt in range(1, 6):  # Faça 5 tentativas
    try:
        app = create_app()
        break  # Se a criação do aplicativo for bem-sucedida, saia do loop
    except Exception as e:
        print(f"Attempt {attempt}: Error creating app: {e}")
        print("Retrying in 5 seconds...")
        time.sleep(5)  # Espere 5 segundos antes de tentar novamente

# Se o aplicativo não puder ser criado após várias tentativas, encerre o script
if app is None:
    print("Failed to create app after multiple attempts. Exiting.")
    exit(1)

# Execute o aplicativo Flask no host e porta especificados
if __name__ == "__main__":
    # Use os.getenv para acessar as variáveis de ambiente do .env
    app.run(host=os.getenv('FLASK_RUN_HOST', '0.0.0.0'), port=os.getenv('FLASK_RUN_PORT', 5001), debug=True)