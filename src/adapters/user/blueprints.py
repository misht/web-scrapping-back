import flask
from src.domain.base import Blueprint, MapperBind, UseCaseBind


class UserBlueprint(Blueprint):
    @staticmethod
    def create(use_cases: UseCaseBind, mappers: MapperBind):
        blueprint = flask.Blueprint('user', __name__)

        @blueprint.route('/sign_up', methods=('POST',))
        def sign_up():
            user = mappers.user_mapper.from_dict(flask.request.get_json())
            saved_user = use_cases.user_use_case.sign_up(user)
            return flask.jsonify(mappers.user_mapper.to_dict(saved_user))

        return blueprint

