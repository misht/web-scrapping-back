import flask
from src.domain.base import Blueprint, UseCaseBind


class PublicationBlueprint(Blueprint):
    @staticmethod
    def create(use_cases: UseCaseBind):
        blueprint = flask.Blueprint('publications', __name__)

        @blueprint.route('/search_publications', methods=('GET',))
        def search_publications():
            query = flask.request.args.get("query")
            publications = use_cases.publication_use_case.search_publications(query)
            return flask.jsonify(publications)

        return blueprint