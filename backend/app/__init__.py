from flask import Flask
import pyodbc

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados SQL Server
    app.config['SQL_SERVER_DATABASE_URI'] = 'Driver={SQL Server};Server=server_name;Database=database_name;Trusted_Connection=yes;'

    # Conexão com o banco de dados
    try:
        connection = pyodbc.connect(app.config['SQL_SERVER_DATABASE_URI'])
        print("Conexão bem-sucedida!")
    except Exception as e:
        print("Erro ao conectar com o banco de dados:", e)

    from .routes import main
    app.register_blueprint(main)

    return app
