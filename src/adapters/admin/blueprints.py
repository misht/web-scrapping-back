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
            response = flask.jsonify(mappers.config_mapper.to_dict(saved_config))
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        return blueprint