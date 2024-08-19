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

        @blueprint.route('/privacy_terms', methods=('GET',))
        def get_privacy_terms():
            privacy_terms = use_cases.user_use_case.get_privacy_terms()
            return flask.jsonify(mappers.config_mapper.to_dict(privacy_terms))

        @blueprint.route('/user_terms', methods=('GET',))
        def get_user_terms():
            user_terms = use_cases.user_use_case.get_user_terms()
            return flask.jsonify(mappers.config_mapper.to_dict(user_terms))

        return blueprint