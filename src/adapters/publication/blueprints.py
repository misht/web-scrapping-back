import flask
from src.domain.base import Blueprint, UseCaseBind


class PublicationBlueprint(Blueprint):
    @staticmethod
    def create(use_cases: UseCaseBind):
        blueprint = flask.Blueprint('publication', __name__)

        @blueprint.route('/search_publications', methods=('GET',))
        def search_publications():
            query = flask.request.args.get("query")
            start = flask.request.args.get("start", 0)
            publications = use_cases.publication_use_case.search_publications(query, int(start))
            response = flask.jsonify(publications)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        return blueprint