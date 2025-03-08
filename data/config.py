import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
con = sqlite3.connect("jogos.db")
cur = con.cursor()

cur.execute("SELECT * FROM jogos WHERE id = 1;")

# Buscar todas as tabelas
tabelas = cur.fetchall()
print(tabelas)

# Salvar alterações e fechar conexão
con.commit()
con.close()

