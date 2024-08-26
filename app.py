import config
import flask
from flask_cors import CORS

import src
from src.bind import Bind
from src.domain.base import Error
import firebase_admin
from firebase_admin import credentials, firestore

app = None
bind = None


def register_blueprints():
    for blueprint in bind.blueprints:
        app.register_blueprint(blueprint, url_prefix='/api')


def initialize_bd():
    cred = credentials.Certificate(
        "./src/wecollaborate1-10579-firebase-adminsdk-lst8w-494ba04746.json")
    firebase_admin.initialize_app(cred)


def create_app():
    global app
    global bind
    if app is None:
        app = flask.Flask(__name__)
        CORS(app)
        # configuration = config.get_config()
        # app.config.from_object(configuration)
        # app.config.from_pyfile('config.py', silent=True)
        initialize_bd()
        bind = Bind()
        register_blueprints()

        @app.route('/')
        def hello():
            return 'Welcome to Web Scrapping!'


create_app()
