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
            response = flask.jsonify(mappers.author_info_mapper.to_dict(author))
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        @blueprint.route('/search_authors_by_interests', methods=('GET',))
        def search_authors_by_interests():
            label = flask.request.args.get("label")
            next_page = flask.request.args.get("next_page")
            previous_page = flask.request.args.get("previous_page")
            authors, pagination = use_cases.author_use_case.search_authors_by_interests(label, next_page, previous_page)
            response_dict = {"authors": [mappers.author_mapper.to_dict(author) for author in authors]}
            response_dict.update(mappers.pagination_mapper.to_dict(pagination))
            response = flask.jsonify(response_dict)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        return blueprint