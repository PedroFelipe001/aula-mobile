from pymongo import MongoClient

# Criar uma conexão com o banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
database = client['sistema_pontuacao']
collection = database['usuarios']

# Função para inserir um novo usuário no banco de dados
def inserir_usuario(nome, email, senha, pontuacao):
    usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'pontuacao': pontuacao
    }
    collection.insert_one(usuario)
    print("Usuário inserido com sucesso!")

# Função para buscar um usuário pelo e-mail
def buscar_usuario_por_email(email):
    usuario = collection.find_one({'email': email})
    if usuario:
        print("Nome:", usuario['nome'])
        print("E-mail:", usuario['email'])
        print("Senha:", usuario['senha'])
        print("Pontuação:", usuario['pontuacao'])
    else:
        print("Usuário não encontrado.")

# Exemplo de uso das funções
inserir_usuario('João', 'joao@example.com', 'senha123', 100)
buscar_usuario_por_email('joao@example.com')

# Função para registrar a pontuação de um usuário
def registrar_pontuacao(email, pontuacao):
    collection.update_one({'email': email}, {'$inc': {'pontuacao': pontuacao}})
    print("Pontuação registrada com sucesso!")

# Função para obter a pontuação de um usuário
def obter_pontuacao(email):
    usuario = collection.find_one({'email': email})
    if usuario:
        print("Pontuação de", usuario['nome'], ":", usuario['pontuacao'])
    else:
        print("Usuário não encontrado.")

# Exemplo de uso das funções
registrar_pontuacao('joao@example.com', 10)  # Adicionar 10 pontos para o usuário 'joao@example.com'
obter_pontuacao('joao@example.com')  # Obter a pontuação do usuário 'joao@example.com'

# Criar uma conexão com o banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
database = client['sistema_pontuacao']
collection = database['usuarios']

# Função para calcular a contagem total de pontuação
def calcular_contagem_pontuacao_total():
    pipeline = [
        {
            '$group': {
                '_id': None,
                'pontuacao_total': {
                    '$sum': '$pontuacao'
                }
            }
        }
    ]

    result = list(collection.aggregate(pipeline))

    if result:
        pontuacao_total = result[0]['pontuacao_total']
        print("Contagem total de pontuação: ", pontuacao_total)
    else:
        print("Não há dados de pontuação.")

# Exemplo de uso da função
calcular_contagem_pontuacao_total()
