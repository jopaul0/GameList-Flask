from app import app
from app.controllers.jogos_controller import *
from app.controllers.login_controller import *
from flask import render_template, request, redirect, url_for, jsonify, session


@app.route("/")
def home():
    jogos = obter_jogos()
    return render_template("index.html", jogos = jogos)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/lista")
@login_required
def jogos():
    jogos = obter_jogos()
    return render_template("lista.html", jogos=jogos)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    response = adicionar_jogos()
    return response
    

@app.route('/listar', methods=['POST'])
def listar():
    response = atualizar_jogos()
    return jsonify({"tabela": response}), 200

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    response = adicionar_usuarios()
    return response

@app.route('/login', methods=['POST'])
def login():
    response = logar_usuario()
    return response

@app.route('/logout')
def logout():
    session.clear()  # Limpa todos os dados da sessão
    return redirect(url_for('home'))