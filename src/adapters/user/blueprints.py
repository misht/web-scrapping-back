import flask
from src.domain.base import Blueprint


class UserBlueprint(Blueprint):
    @staticmethod
    def create():
        blueprint = flask.Blueprint('users', __name__)

        @blueprint.route('/login', methods=('GET',))
        def login():
            return flask.jsonify({"usuario" : "Pedro"})

        return blueprint
