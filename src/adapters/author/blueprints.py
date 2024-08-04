import flask
from src.domain.base import Blueprint, UseCaseBind, MapperBind


class AuthorBlueprint(Blueprint):
    @staticmethod
    def create(use_cases: UseCaseBind, mappers: MapperBind):
        blueprint = flask.Blueprint('author', __name__)

        @blueprint.route('/search_author_id', methods=('GET',))
        def search_author_id():
            author_id = flask.request.args.get("author_id")
            author = use_cases.author_use_case.search_author_id(author_id)
            response = flask.jsonify(mappers.author_mapper.to_dict(author))
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        return blueprint