import os

#Rota do banco de dados
DB_PATH = "data/jogos.txt"

#Classe Jogos
class Jogos:
    #Construtor da classe
    def __init__(self, ano, nome, descricao, plataforma):
        self.nome = nome
        self.descricao = descricao
        self.plataforma = plataforma
        self.ano = ano

    #Lista os jogos existentes no banco de dados
    def listar():
        #Verifica se o arquivo existe
        if not os.path.exists(DB_PATH):
            return []

        #Abre o arquivo e retorna os jogos
        jogos = []
        with open(DB_PATH, "r", encoding="utf-8") as file:
            for linha in file.readlines():
                dados = linha.strip().split(";")
                if len(dados) == 4:
                    jogos.append(Jogos(dados[0], dados[1], dados[2], dados[3]))
        return jogos
    
    #Adiciona um jogo ao banco de dados
    def adicionar(ano, nome, descricao, plataforma):
        #Abre o arquivo em modo de escrita
        with open(DB_PATH, "a", encoding="utf-8") as file:
            #Escreve o jogo no arquivo
            file.write(f"{ano};{nome};{descricao};{plataforma}\n")
        return True
             