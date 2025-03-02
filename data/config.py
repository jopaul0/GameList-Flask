import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
con = sqlite3.connect("jogos.db")
cur = con.cursor()

cur.execute("SELECT * FROM jogos;")
jogos = cur.fetchall()

print("Lista de jogos cadastrados:")
for jogo in jogos:
    print(jogo)



# Salvar alterações e fechar conexão
con.commit()
con.close()

