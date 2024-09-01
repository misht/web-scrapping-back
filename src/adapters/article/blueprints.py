import flask
from src.domain.base import Blueprint, UseCaseBind, MapperBind


class ArticleBlueprint(Blueprint):
    @staticmethod
    def create(use_cases: UseCaseBind, mappers: MapperBind):
        blueprint = flask.Blueprint('article', __name__)

        @blueprint.route('/search_articles', methods=('GET',))
        def search_articles():
            query = flask.request.args.get("query")
            start = flask.request.args.get("start", 0)
            articles = use_cases.article_use_case.search_articles(query, int(start))
            response = flask.jsonify([mappers.second_article_mapper.to_dict(article) for article in articles])
            return response

        @blueprint.route('/search_articles_and_authors', methods=('GET',))
        def search_articles_and_authors():
            query = flask.request.args.get("query")
            label = flask.request.args.get("label")
            articles, authors = use_cases.article_use_case.search_articles_and_authors(query, label)
            response = flask.jsonify(
                {"authors": [mappers.author_mapper.to_dict(author) for author in authors],
                "articles": [mappers.second_article_mapper.to_dict(article) for article in articles]})
            return response

        return blueprint