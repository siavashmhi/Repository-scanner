from flask import Flask

from .view.v1 import apiv1_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(apiv1_bp)
    return app
