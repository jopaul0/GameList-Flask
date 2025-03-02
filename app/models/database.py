import sqlite3

class Database:
    #Construtor
    def __init__(self, db_path):
        self.db_path = db_path
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()
    
    #Executa uma query no banco de dados
    def query(self, query, params=()):
        self.cur.execute(query, params)
    
    # Obtém os nomes das colunas a partir de cursor.description
        columns = [column[0] for column in self.cur.description]
    
    # Recupera todas as linhas e cria uma lista de dicionários
        rows = self.cur.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
    
        return result

    
    #Salva as alterações e fecha a conexão
    def close(self):
        self.con.commit()
        self.con.close()