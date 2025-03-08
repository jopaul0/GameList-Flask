from app.models.jogos import Jogos
from werkzeug.utils import secure_filename
from app import app
from flask import render_template, request, redirect, url_for, jsonify
import os
import uuid
from datetime import datetime

#Obtem os jogos
def obter_jogos():
    return Jogos.listar()

#Adiciona um jogo
def adicionar_jogos():
    try:
        UPLOAD_FOLDER = "static/uploads"
        app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

        # Recebe os dados do formulário
        ano = request.form.get('ano')
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        plataforma = request.form.get('plataforma')
        genero = request.form.get('genero')

        # Verifica se todos os campos obrigatórios estão preenchidos
        if not ano or not nome or not descricao or not plataforma or not genero:
            return jsonify({"erro": "Todos os campos devem ser preenchidos!"}), 400

        # Verifica se o arquivo de foto foi enviado
        if 'foto' not in request.files:
            return jsonify({"erro": "Nenhuma imagem enviada!"}), 400

        foto = request.files['foto']

        # Verifica se o arquivo foi selecionado
        if foto.filename == "":
            return jsonify({"erro": "Nenhuma imagem selecionada!"}), 400

        # Verifica se o arquivo tem uma extensão válida
        if foto and allowed_file(foto.filename):
            # Obtém a extensão do arquivo
            ext = os.path.splitext(foto.filename)[1]

            # Cria um nome único usando UUID e timestamp
            unique_filename = f"{uuid.uuid4().hex}_{datetime.now().strftime('%Y%m%d%H%M%S')}{ext}"
            secure_name = secure_filename(unique_filename)  # Garante que o nome seja seguro
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_name)

            # Salva o arquivo na pasta de uploads
            foto.save(filepath)

            # Define a URL da foto para ser armazenada no banco de dados
            foto_url = f"/{UPLOAD_FOLDER}/{secure_name}"

            # Chama a função de adicionar jogo no banco de dados
            response = Jogos.adicionar(ano, nome, descricao, plataforma, genero, foto_url)
            if response:
                return jsonify({"mensagem": "Jogo adicionado com sucesso!"}), 200
            else:
                return jsonify({"erro": "Erro ao adicionar jogo no banco!"}), 500
        else:
            return jsonify({"erro": "Extensão de arquivo inválida!"}), 400
    except Exception as e:
        print(f"Erro no servidor: {e}")  # Log do erro para análise no servidor
        return jsonify({"erro": "Erro interno no servidor!"}), 500
  

#verifica se a extensão do arquivo é permitida
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Atualiza a tabela
def atualizar_jogos():
    jogos = Jogos.listar()
    response = ""
    for jogo in jogos:
        response += f"<tr class='jogo' data-id='{ jogo["id"] }' data-genero='{ jogo["genero"] }' data-ano='{ jogo["ano_lancamento"] }' data-nome='{ jogo["nome"] }' data-descricao='{ jogo["descricao"] }' data-plataforma='{ jogo["plataforma"] }'><td>{jogo['ano_lancamento']}</td><td>{jogo['nome']}</td><td>{jogo['descricao']}</td><td>{jogo['plataforma']}</td><td><img src='{jogo['foto']}' alt='Imagem do jogo' width='50' height='50'/></td><td>{jogo['genero']}</td></tr>"
    return response

def editar_jogos():
    try:
        UPLOAD_FOLDER = "static/uploads"
        app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

        # Recebe os dados do formulário
        jogo_id = request.form.get('id')  # Adicione um identificador do jogo
        ano = request.form.get('ano')
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        plataforma = request.form.get('plataforma')
        genero = request.form.get('genero')

        # Verifica se todos os campos obrigatórios estão preenchidos
        if not jogo_id or not ano or not nome or not descricao or not plataforma or not genero:
            return jsonify({"erro": "Todos os campos devem ser preenchidos!"}), 400

        # Obtém o jogo existente no banco de dados para recuperar a foto atual
        jogo_existente = Jogos.buscar_por_id(jogo_id)
        if not jogo_existente:
            return jsonify({"erro": "Jogo não encontrado!"}), 404

        
        foto_url = jogo_existente[0]['foto']  # Mantém a foto atual
       
        # Verifica se o arquivo de foto foi enviado
        if 'foto' in request.files:
            print("aqui")
            foto = request.files['foto']

            # Se um novo arquivo foi enviado, processamos a nova foto
            if foto.filename != "":
                if allowed_file(foto.filename):
                    ext = os.path.splitext(foto.filename)[1]
                    unique_filename = f"{uuid.uuid4().hex}_{datetime.now().strftime('%Y%m%d%H%M%S')}{ext}"
                    secure_name = secure_filename(unique_filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_name)

                    foto.save(filepath)
                    foto_url = f"/{UPLOAD_FOLDER}/{secure_name}"  # Atualiza a URL da foto
                else:
                    return jsonify({"erro": "Extensão de arquivo inválida!"}), 400

        # Atualiza os dados do jogo no banco de dados
        response = Jogos.atualizar(jogo_id, ano, nome, descricao, plataforma, genero, foto_url)
        if response:
            return jsonify({"mensagem": "Jogo atualizado com sucesso!"}), 200
        else:
            return jsonify({"erro": "Erro ao atualizar jogo no banco!"}), 500
    except Exception as e:
        print(f"Erro no servidor: {e}")
        return jsonify({"erro": "Erro interno no servidor!"}), 500

def excluir_jogos():
    try:
        jogo_id = request.form.get('id')
        if not jogo_id:
            return jsonify({"erro": "ID do jogo não informado!"}), 400

        response = Jogos.remover(jogo_id)
        if response:
            return jsonify({"mensagem": "Jogo excluído com sucesso!"}), 200
        else:
            return jsonify({"erro": "Erro ao excluir jogo!"}), 500
    except Exception as e:
        print(f"Erro no servidor: {e}")
        return jsonify({"erro": "Erro interno no servidor!"}), 500
