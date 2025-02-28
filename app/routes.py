from app import app
from app.controllers.jogos_controller import obter_jogos
from flask import render_template, request, redirect, url_for

@app.route("/")
def index():
    jogos = obter_jogos()
    return render_template("index.html", jogos=jogos)

