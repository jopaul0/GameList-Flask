from app import app
from app.controllers.jogos_controller import *
from flask import render_template, request, redirect, url_for, jsonify

@app.route("/")
def home():
    jogos = obter_jogos()
    return render_template("index.html", jogos = jogos)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/lista")
def index():
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
