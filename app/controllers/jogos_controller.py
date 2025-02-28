from app.models.jogos import Jogos

#Obtem os jogos
def obter_jogos():
    return Jogos.listar()