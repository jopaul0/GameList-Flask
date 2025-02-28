from app import app
from app.controllers.jogos_controller import *
from flask import render_template, request, redirect, url_for, jsonify

@app.route("/")
def index():
    jogos = obter_jogos()
    return render_template("index.html", jogos=jogos)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    ano = request.form['ano']
    nome = request.form['nome']
    descricao = request.form['descricao']
    plataforma = request.form['plataforma']
    adicionar_jogos(ano, nome, descricao, plataforma)
    return jsonify({"mensagem": "Jogo adicionado com sucesso!"}), 200

@app.route('/listar', methods=['POST'])
def listar():
    response = atualizar_jogos()
    return jsonify({"tabela": response}), 200
