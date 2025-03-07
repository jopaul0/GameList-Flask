import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
con = sqlite3.connect("jogos.db")
cur = con.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Buscar todas as tabelas
tabelas = cur.fetchall()

# Mostrar as tabelas
if tabelas:
    print("Tabelas existentes no banco de dados:")
    for tabela in tabelas:
        print(tabela[0])  # Cada item de 'tabelas' é uma tupla (nome_da_tabela,)
else:
    print("Não há tabelas no banco de dados.")

# Salvar alterações e fechar conexão
con.commit()
con.close()

