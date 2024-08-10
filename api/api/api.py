from flask import Flask

from .config import Config
from .object import db, mg
from .view import apiv1_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    mg.init_app(app, db)
    app.register_blueprint(apiv1_bp)
    print(app.config)
    return app
