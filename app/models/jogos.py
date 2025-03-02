from app.models.database import Database

#Rota do banco de dados
DB_PATH = "data/jogos.db"

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
    def adicionar(ano, nome, descricao, plataforma):
        #Abre o arquivo em modo de escrita
        with open(DB_PATH, "a", encoding="utf-8") as file:
            #Escreve o jogo no arquivo
            file.write(f"{ano};{nome};{descricao};{plataforma}\n")
        return True
             