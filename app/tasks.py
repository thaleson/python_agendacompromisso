from app import mail, db
from flask_mail import Message
from app.models import Evento
from flask import render_template
from app import create_app

def enviar_email_lembrete(evento_id):
    app = create_app()
    with app.app_context():
        evento = Evento.query.get(evento_id)
        if evento and not evento.enviado:
            msg = Message(
                subject=f"Lembrete: {evento.titulo}",
                recipients=[evento.email],
                html=render_template('email_lembrete.html', evento=evento)
            )
            mail.send(msg)
            evento.enviado = True
            db.session.commit()
