import config
import flask
import src
from src.bind import Bind
from src.domain.base import Error
from scholarly import scholarly

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
            print("Búsqueda de autor por organización: (Juan Tamargo)")
            search_query = scholarly.search_author_by_organization(3310657935946510136)
            author = next(search_query)
            scholarly.pprint(scholarly.fill(author, sections=['basics']))
            print("Búsqueda de autor por su id: (Juan Antonio Clemente)")
            search_query = scholarly.search_author_id('71ZyPn0AAAAJ')
            scholarly.pprint(scholarly.fill(search_query, sections=['basics']))
            print("Búsqueda por autor: (Juan Antonio Clemente)") # No lo reconoce bien
            search_query = scholarly.search_author('Juan Antonio Clemente')
            author = next(search_query)
            scholarly.pprint(scholarly.fill(author, sections=['basics']))
            print("Búsqueda por autor: (Juan Antonio Clemente, Universidad Complutense de Madrid)")  # Lo reconoce bien
            search_query = scholarly.search_author('Juan Antonio Clemente, Universidad Complutense de Madrid')
            author = next(search_query)
            scholarly.pprint(scholarly.fill(author, sections=['basics', 'counts', 'coauthors', 'publications']))
            print("Búsqueda por organización: ")
            search_query = scholarly.search_org('Princeton University')
            print(search_query)
            print("Búsqueda por artículos/publicaciones: ")
            search_query = scholarly.search_pubs('Cancer')
            scholarly.pprint(next(search_query))
            return 'Welcome to Web Scrapping!'


create_app()
