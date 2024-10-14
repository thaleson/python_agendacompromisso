from datetime import datetime, timedelta, timezone
from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import EventoForm
from app import db, q
from app.models import Evento
from app.tasks import enviar_email_lembrete

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    eventos = Evento.query.order_by(Evento.data_evento.asc()).all()
    return render_template('index.html', eventos=eventos)

@bp.route('/adicionar', methods=['GET', 'POST'])
def adicionar_evento():
    form = EventoForm()
    if form.validate_on_submit():
        evento = Evento(
            titulo=form.titulo.data,
            descricao=form.descricao.data,
            data_evento=form.data_evento.data,
            email=form.email.data
        )
        db.session.add(evento)
        db.session.commit()

        # Usar datetime.now() com timezone UTC
        now = datetime.now(timezone.utc)
        event_time = evento.data_evento

        # Garantir que o 'data_evento' seja ciente do timezone
        if event_time.tzinfo is None:
            event_time = event_time.replace(tzinfo=timezone.utc)

        delay = (event_time - now).total_seconds()
        delay = max(delay, 0)  # Evitar delays negativos

        # Agendar a tarefa no RQ para enviar o email na data do evento
        q.enqueue_in(timedelta(seconds=delay), enviar_email_lembrete, evento.id)

        flash('Evento adicionado com sucesso!', 'success')
        return redirect(url_for('main.index'))
    return render_template('adicionar_evento.html', form=form)
