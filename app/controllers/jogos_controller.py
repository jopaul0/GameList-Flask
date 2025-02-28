from app.models.jogos import Jogos


#Obtem os jogos
def obter_jogos():
    return Jogos.listar()

#Adiciona um jogo
def adicionar_jogos(ano, nome, descricao, plataforma):
    return Jogos.adicionar(ano, nome, descricao, plataforma)

#Atualiza a tabela
def atualizar_jogos():
    jogos = Jogos.listar()
    response = ""
    for jogo in jogos:
        response += f"<tr><td>{jogo.ano}</td><td>{jogo.nome}</td><td>{jogo.descricao}</td><td>{jogo.plataforma}</td></tr>"
    return response