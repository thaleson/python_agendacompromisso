from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from redis import Redis
from rq import Queue
from config import Config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
redis_conn = Redis.from_url(Config.REDIS_URL)
q = Queue('default', connection=redis_conn)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Importar modelos para que o Flask-Migrate possa detectá-los
    from app import models

    # Registrar blueprints ou rotas
    from app.routes import bp
    app.register_blueprint(bp)

    return app
