from flask import Flask

from .config import Config
from .view import apiv1_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(apiv1_bp)
    print(app.config)
    return app
