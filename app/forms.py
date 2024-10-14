from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Email

class EventoForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descricao = TextAreaField('Descrição')
    data_evento = DateTimeField('Data e Hora do Evento (DD/MM/YYYY HH:MM)', format='%d/%m/%Y %H:%M', validators=[DataRequired()])
    email = StringField('Email para Envio do Lembrete', validators=[DataRequired(), Email()])
    submit = SubmitField('Adicionar Evento')
