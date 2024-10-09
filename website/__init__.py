from flask import Flask
from conifg import KEYS

def create_app():
    app = Flask(__name__)
    app.config[KEYS.SECRET_KEY]

    return app