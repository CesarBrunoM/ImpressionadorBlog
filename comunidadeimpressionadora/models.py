from comunidadeimpressionadora import database, login_maneger
from datetime import datetime
from flask_login import UserMixin


@login_maneger.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    post = database.relationship('Post', backref='autor', lazy=True)
    # cursos = database.relationship('Curso_aluno', backref='aluno', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não informado')


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


'''class Curso_aluno(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_aluno = database.Column(database.Integer, database.ForeignKey('usuario.ip'), nullable=False)
    curso = database.Column(database.String, nullable=False)'''
