import config
import flask
import src
from src.bind import Bind
from src.domain.base import Error

app = None
bind = None


def register_blueprints():
    for blueprint in bind.blueprints:
        app.register_blueprint(blueprint, url_prefix='/api')


def create_app():
    global app
    global bind
    if app is None:
        app = flask.Flask(__name__)
        # configuration = config.get_config()
        # app.config.from_object(configuration)
        # app.config.from_pyfile('config.py', silent=True)

        bind = Bind()
        register_blueprints()

        @app.route('/')
        def hello():
            return 'Welcome to Web Scrapping!'


create_app()
