from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# csrf_token

app.config['SECRET_KEY'] = 'ba803396da27d250f78029201b019681'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

from comunidadeimpressionadora import routes