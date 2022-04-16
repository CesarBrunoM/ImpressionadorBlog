from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(message='Preenchimento do campo obrigatório.')])
    email = StringField('E-mail', validators=[DataRequired(), Email(message='E-mail inválido.')])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20, message='A senha deve conter de 6 a 20 caracteres.')])
    confirmacao = PasswordField('Confirmação de senha', validators=[DataRequired(), EqualTo('senha', message='As senhas não conferem.')])
    botao_submit_criarconta = SubmitField('Criar conta')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email('E-mail inválido.')])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20, message='A senha deve conter de 6 a 20 caracteres.')])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_submit_login = SubmitField('Entrar')
