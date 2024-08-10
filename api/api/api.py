from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .view import apiv1_bp

db = SQLAlchemy()
mg = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    mg.init_app(app, db)
    app.register_blueprint(apiv1_bp)
    print(app.config)
    return app
