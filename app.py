import config
import flask
import src
from src.bind import Bind
from src.domain.base import Error
from flask_sqlalchemy import SQLAlchemy


app = None
bind = None
db = None


def register_blueprints():
    for blueprint in bind.blueprints:
        app.register_blueprint(blueprint, url_prefix='/api')


def create_app():
    global app
    global bind
    global db
    if app is None:
        # Create db extension
        db = SQLAlchemy()
        # Create the app
        app = flask.Flask(__name__)
        # Configure the SQLite database, relative to the app instance folder
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:web2023@localhost/web-scrapping-database"
        # Initialize the app with the extension
        db.init_app(app)
        # configuration = config.get_config()
        # app.config.from_object(configuration)
        # app.config.from_pyfile('config.py', silent=True)
        bind = Bind()
        register_blueprints()

        @app.route('/')
        def hello():
            return 'Welcome to Web Scrapping!'


create_app()
