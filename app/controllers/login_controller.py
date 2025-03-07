from flask import render_template, request, redirect, url_for, jsonify, session
from app.models.usuarios import Usuario
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function
    
def adicionar_usuarios():
    try:
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        telefone = request.form.get('telefone')

        if not nome or not email or not senha or not telefone:
            return jsonify({"erro": "Todos os campos devem ser preenchidos!"}), 400
        
        response = Usuario.cadastrar(nome, email, senha, telefone)
        if response:
            return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 200
        else:
            return jsonify({"erro": "Erro ao cadastrar usuário!"}), 400
    except Exception as e:
        print(e)
        return jsonify({"erro": "Erro ao cadastrar usuário!"}), 400
    
def logar_usuario():
    try:
        email = request.form.get('email')
        senha = request.form.get('password')
      
        response = Usuario.logar(email, senha)
        if response:
            return jsonify({"mensagem": "Usuário logado com sucesso!"}), 200
        else:
            print('Erro ao logar usuário!')
            return jsonify({"erro": "Erro ao logar usuário!"}), 400
    except Exception as e:
        print(e)
        return jsonify({"erro": "Erro ao logar usuário!"}), 400