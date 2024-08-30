import flask
from src.domain.base import Blueprint, MapperBind, UseCaseBind


class ConfigBlueprint(Blueprint):
    @staticmethod
    def create(use_cases: UseCaseBind, mappers: MapperBind):
        blueprint = flask.Blueprint('config', __name__)

        @blueprint.route('/config', methods=('POST',))
        def add_config():
            config = mappers.config_mapper.from_dict(flask.request.get_json())
            saved_config = use_cases.config_use_case.add_config(config)
            return flask.jsonify(mappers.config_mapper.to_dict(saved_config))

        @blueprint.route('/interest', methods=('POST',))
        def add_interest():
            interest = mappers.interest_admin_mapper.from_dict(flask.request.get_json())
            saved_interest = use_cases.interest_use_case.add_interest(interest)
            return flask.jsonify(mappers.interest_mapper.to_dict(saved_interest))

        @blueprint.route('/interest', methods=('PUT',))
        def edit_interest():
            interest = mappers.interest_admin_mapper.from_dict(flask.request.get_json())
            saved_interest = use_cases.interest_use_case.edit_interest(interest)
            return flask.jsonify(mappers.interest_mapper.to_dict(saved_interest))

        @blueprint.route('/interest', methods=('DELETE',))
        def delete_interest():
            interest = mappers.interest_admin_mapper.from_dict(flask.request.get_json())
            saved_interest = use_cases.interest_use_case.delete_interest(interest)
            return flask.jsonify(mappers.interest_mapper.to_dict(saved_interest))

        return blueprint