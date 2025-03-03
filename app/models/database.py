import sqlite3

#Rota do banco de dados
DB_PATH = "data/jogos.db"

class Database:
    #Construtor
    def __init__(self, db_path):
        self.db_path = db_path
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()
    
    #Executa uma query no banco de dados
    def query(self, query, params=()):
        self.cur.execute(query, params)
    
    # Se for um comando SELECT, retorna os resultados
        if query.strip().upper().startswith("SELECT"):
            columns = [column[0] for column in self.cur.description]
            rows = self.cur.fetchall()
            return [dict(zip(columns, row)) for row in rows]
    
        return True

    
    #Salva as alterações e fecha a conexão
    def close(self):
        self.con.commit()
        self.con.close()