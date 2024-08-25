import pyodbc
# Aqui você definirá os modelos de dados
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-P1CORCC\SQLEXPRESS01;"
    "Database=FluxoDeCaixa;"
    )

# Conexão com o banco de dados
try:
    conexao = pyodbc.connect(dados_conexao)
    print("Conexão bem-sucedida!")
except Exception as e:
    print("Erro ao conectar com o banco de dados:", e)


cursor = conexao.cursor()

# Solicitando o ID do cliente para buscar o nome
cliente_id = input("Informe o ID do cliente: ")

# Consulta para obter o nome do cliente a partir do ID
comando_select = f"SELECT NomeCliente FROM DimCliente WHERE ClienteID = {cliente_id}"

# Executando a consulta
cursor.execute(comando_select)

# Recuperando o resultado
resultado = cursor.fetchone()

# Verificando se o cliente foi encontrado
if resultado:
    print(f"O nome do cliente com ID {cliente_id} é: {resultado[0]}")
else:
    print(f"Cliente com ID {cliente_id} não encontrado.")

# Fechando a conexão
conexao.close()
