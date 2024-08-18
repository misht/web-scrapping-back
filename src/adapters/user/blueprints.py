import flask
from src.domain.base import Blueprint, MapperBind, UseCaseBind


class UserBlueprint(Blueprint):
    @staticmethod
    def create(use_cases: UseCaseBind, mappers: MapperBind):
        blueprint = flask.Blueprint('user', __name__)

        @blueprint.route('/login', methods=('GET',))
        def login():
            user = mappers.user_login_mapper.from_dict(flask.request.get_json())
            logged_user = use_cases.user_use_case.login(user)
            return flask.jsonify(mappers.user_mapper.to_dict(logged_user))

        @blueprint.route('/sign_up', methods=('POST',))
        def sign_up():
            user = mappers.user_mapper.from_dict(flask.request.get_json())
            saved_user = use_cases.user_use_case.sign_up(user)
            return flask.jsonify(mappers.user_mapper.to_dict(saved_user))

        return blueprint

