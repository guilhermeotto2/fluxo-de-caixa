import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-P1CORCC\SQLEXPRESS01;"
    "Database=FluxoDeCaixa;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

nome = input("Infome seu nome: ")

cpf = input("Infome seu CPF: ")

nascimento = input("Infome sua data de nacimento (xx/xx/xxxx): ")

endereco = input("Infome seu endereço ")

cidade = input("Infome sua cidade: ")

estado = input("Infome seu estado: ")

comando = f"""Insert into DimCliente(NomeCliente, CPF, DataNascimento, Endereco, Cidade, Estado)
VALUES
	('{nome}', '{cpf}', '{nascimento}', '{endereco}', '{cidade}', '{estado}') """

cursor.execute(comando)
cursor.commit()