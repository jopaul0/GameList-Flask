from app.models.database import *



#Classe Jogos
class Jogos:
    #Construtor
    def __init__(self, ano, nome, descricao, genero, plataforma, foto):
        self.ano = ano
        self.nome = nome
        self.descricao = descricao
        self.genero = genero
        self.plataforma = plataforma
        self.foto = foto

    #Lista os jogos existentes no banco de dados
    def listar():
        data = Database(DB_PATH)
        jogos = data.query("SELECT * FROM jogos;")
        data.close()
        return jogos
    
    #Adiciona um jogo ao banco de dados
    def adicionar(ano, nome, descricao, plataforma, genero, foto):
        try:
            data = Database(DB_PATH)
            data.query("INSERT INTO jogos (ano_lancamento, nome, descricao, plataforma, genero, foto) VALUES (?, ?, ?, ?, ?, ?);", (ano, nome, descricao, plataforma, genero, foto))
            data.close()
            return True
        except Exception as e:
            print(e)
            return False

             