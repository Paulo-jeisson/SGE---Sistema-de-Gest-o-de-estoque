# SGE - Sistema de Gestão de Estoque

Sistema web desenvolvido em Django para controle de estoque, produtos, categorias, marcas, fornecedores e movimentações.

## Sobre o projeto

O SGE tem como objetivo facilitar o gerenciamento de estoque de pequenas empresas, permitindo cadastrar produtos, controlar entradas e saídas, organizar fornecedores e acompanhar informações importantes do negócio em um painel administrativo.

## Tecnologias utilizadas

* Python
* Django
* Django REST Framework
* SQLite
* HTML
* CSS
* Bootstrap
* JavaScript
* Git e GitHub

## Funcionalidades

* Cadastro de produtos
* Cadastro de categorias
* Cadastro de marcas
* Cadastro de fornecedores
* Controle de estoque
* Autenticação de usuários
* API com Django REST Framework
* Painel administrativo
* Interface web responsiva

## Como rodar o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd sge
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py migrate
```

Crie um superusuário:

```bash
python manage.py createsuperuser
```

Rode o servidor:

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```

## Status do projeto

Projeto em desenvolvimento, com melhorias contínuas na interface, API e regras de negócio.

## Autor

Desenvolvido por Paulo Jeisson Costa.
