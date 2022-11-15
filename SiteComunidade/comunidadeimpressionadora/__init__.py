# CONFIGURAÇÃO DO SITE
# CONFIGURAÇÃO DO APP
# CONFIGURAÇÃO DO BANCO DE DADOS

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = '3ac9b3a5750f8a5960cff8f039aacca3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from comunidadeimpressionadora import routes