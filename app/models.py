from app import db
from datetime import datetime

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    data_evento = db.Column(db.DateTime, nullable=False, index=True)
    email = db.Column(db.String(120), nullable=False)
    enviado = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Evento {self.titulo}>'
