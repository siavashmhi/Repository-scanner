from flask import Flask, request, Blueprint
# app = Flask(__name__) ## singleton pattern

ENABLE_V1 = True
ENABLE_V2 = False

## factory pattern 
app_v1 = Blueprint("app_v1", __name__, url_prefix="/v1")
app_v2 = Blueprint("app_v2", __name__, url_prefix="/v2")

@app_v1.route("/test")
def index():
    return f"welcome from v1 your address is {request.remote_addr}"

@app_v2.route("/test")
def welcome_message():
    return f"welcome from v2 your address is {request.remote_addr}"

def create_app(): 
    app = Flask(__name__)
    if ENABLE_V1:
        app.register_blueprint(app_v1)
    if ENABLE_V2:
        app.register_blueprint(app_v2)
    return app
