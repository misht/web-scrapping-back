import flask
from src.domain.base import Blueprint, MapperBind, UseCaseBind


class UserBlueprint(Blueprint):
    @staticmethod
    def create(use_cases: UseCaseBind, mappers: MapperBind):
        blueprint = flask.Blueprint('user', __name__)

        @blueprint.route('/login', methods=('GET',))
        def login():
            email = flask.request.args.get("email")
            logged_user = use_cases.user_use_case.login(email)
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

        @blueprint.route('/user_info', methods=('GET',))
        def get_user_info():
            email = flask.request.args.get("email")
            user_info = use_cases.user_use_case.get_user_info(email)
            return flask.jsonify(mappers.user_info_mapper.to_dict(user_info))

        @blueprint.route('/user_info', methods=('PUT',))
        def edit_user_info():
            user_info = mappers.user_info_mapper.from_dict(flask.request.get_json())
            edited_user_info = use_cases.user_use_case.edit_user_info(user_info)
            return flask.jsonify(mappers.user_info_mapper.to_dict(edited_user_info))

        @blueprint.route('/interests', methods=('GET',))
        def get_interests():
            email = flask.request.args.get("email")
            interests, user_interests = use_cases.user_use_case.get_interests(email)
            return flask.jsonify(mappers.user_interest_mapper.to_dict(interests, user_interests))

        @blueprint.route('/interests', methods=('POST',))
        def add_interests():
            email = flask.request.args.get("email")
            interests = mappers.interests_mapper.from_dict(flask.request.get_json())
            user_info = use_cases.user_use_case.add_interests(interests, email)
            return flask.jsonify(mappers.user_info_mapper.to_dict(user_info))

        return blueprint
