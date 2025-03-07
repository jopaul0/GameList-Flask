from app.models.database import *
from flask import session

class Usuario:
    def __init__(self, nome, email, senha, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone

    def cadastrar(nome, email, senha, telefone):
        try:
            data = Database(DB_PATH)
        
        # Verificando se o email já existe
            resultado = data.query("SELECT 1 FROM usuarios WHERE email = ? LIMIT 1;", (email,))
        
        # Se já existir um email, retornar False
            if resultado:
                print("Email já cadastrado.")
                data.close()
                return False

        # Caso não exista, fazer o cadastro
            data.query("INSERT INTO usuarios (nome, email, senha, telefone) VALUES (?, ?, ?, ?);", (nome, email, senha, telefone))
            data.close()
            return True
        except Exception as e:
            print(e)
            return False

    def logar(email, senha):
        try:
            data = Database(DB_PATH)
            resultado = data.query("SELECT * FROM usuarios WHERE email = ? AND senha = ? LIMIT 1;", (email, senha))
            data.close()

        # Verifica se existe algum resultado
            if resultado:
                print(resultado)

            # O resultado[0] é a primeira linha, os dados começam a partir do índice 0
                usuario = Usuario(resultado[0]['nome'], resultado[0]['email'], resultado[0]['senha'], resultado[0]['telefone'])
                
            # Salva os dados do usuário na sessão
                session['usuario'] = {
                    'nome': usuario.nome,
                    'email': usuario.email,
                    'telefone': usuario.telefone
                }
                
                return True  # Login bem-sucedido
            else:
                return False  # Não encontrou o usuário

        except Exception as e:
            print(e, 'b')
            return False


