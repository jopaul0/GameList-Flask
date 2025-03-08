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
        try:
            data = Database(DB_PATH)
            jogos = data.query("SELECT * FROM jogos;")
            data.close()
            return jogos
        except Exception as e:
            print(e)
            return False
    
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
        
    def atualizar(jogo_id, ano, nome, descricao, plataforma, genero, foto_url):
        try:
            data = Database(DB_PATH)

            data.query("""
                UPDATE jogos 
                SET ano_lancamento = ?, nome = ?, descricao = ?, plataforma = ?, genero = ?, foto = ?
                WHERE id = ?
            """, (ano, nome, descricao, plataforma, genero, foto_url, jogo_id))

            data.close()
            return True  # Retorna True se a atualização for bem-sucedida
        except Exception as e:
            print(f"Erro ao atualizar jogo: {e}")
            return False  # Retorna False se houver erro
        
    def buscar_por_id(jogo_id):
        try:
            data = Database(DB_PATH)
            jogo = data.query("SELECT * FROM jogos WHERE id = ?;", (jogo_id,))
            data.close()
            return jogo
        except Exception as e:
            print(e)
            return False
        
    def remover(jogo_id):
        try:
            data = Database(DB_PATH)
            data.query("DELETE FROM jogos WHERE id = ?;", (jogo_id,))
            data.close()
            return True
        except Exception as e:
            print(e)
            return False

             