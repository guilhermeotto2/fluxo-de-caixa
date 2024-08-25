from flask import Flask
import pyodbc

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados SQL Server
    dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-P1CORCC\SQLEXPRESS01;"
    "Database=FluxoDeCaixa;"
    )

    # Conexão com o banco de dados
    try:
        connection = pyodbc.connect(dados_conexao)
        print("Conexão bem-sucedida!")
    except Exception as e:
        print("Erro ao conectar com o banco de dados:", e)

    from .routes import main
    app.register_blueprint(main)

    return app
