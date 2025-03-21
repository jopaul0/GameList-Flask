# GameList - Flask

Este é um projeto desenvolvido para testar e treinar meus conhecimentos em **Python** como back-end de aplicações web. Para isso, estou utilizando o framework **Flask** juntamente com a **arquitetura MVC** (Model-View-Controller) para organizar o projeto.

## Funcionalidades

O projeto permite que o usuário faça as seguintes operações em uma lista de jogos:

- **Criar**: Adicionar um novo jogo à lista.
- **Ler**: Exibir todos os jogos cadastrados.
- **Atualizar**: Editar as informações de um jogo existente.
- **Deletar**: Remover um jogo da lista.

Essas operações formam um sistema completo de **CRUD** (Create, Read, Update, Delete), possibilitando o gerenciamento de jogos em uma interface simples e funcional.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **Flask**: Framework utilizado para construir a aplicação web.
- **HTML/CSS**: Para a criação das páginas e estilização.
- **SQLite**: Banco de dados utilizado para armazenar as informações dos jogos.

## Estrutura do Projeto

A arquitetura do projeto segue o padrão **MVC** (Model-View-Controller), organizando o código em três camadas principais:

- **Model**: Representa a camada de dados, onde ficam as interações com o banco de dados (CRUD).
- **View**: São as páginas que o usuário vê, em HTML.
- **Controller**: Contém as funções que gerenciam as ações dos usuários e interagem com o Model e a View.
