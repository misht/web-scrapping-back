from typing import Dict, List

from serpapi import GoogleSearch

from config import Configuration
from src.domain.article.model import Article
from src.domain.base import UseCase


class ArticleUseCase(UseCase):

    def __init__(self, author_use_case):
        self.author_use_case = author_use_case

    def search_articles(self, query: str, start: int = 0) -> List[Article]:
        params = {
            "engine": "google_scholar",
            "q": query,
            "api_key": "d9f6757f8c03b67dce2a73f3ab5109697e4c795b6ff63dac5acfad099960a4b1",
            "start": start
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        print(results)
        articles = self.__get_articles__(results.get("organic_results", []))
        return articles

    def __get_articles__(self, organic_results: List[Dict]) -> List[Article]:
        articles = []
        if organic_results:
            for organic_result in organic_results:
                if len(articles) == Configuration.MAX_ARTICLES:
                    break
                articles.append(Article(authors=organic_result.get("publication_info").get("summary"),
                                        cited_by=organic_result.get("inline_links").get("cited_by").get("total", 0),
                                        link=organic_result.get("link"),
                                        title=organic_result.get("title"),
                                        snippet=organic_result.get("snippet")))

        return articles

    def search_articles_and_authors(self, query: str, label: str):
        articles = self.search_articles(query)
        authors, pagination = self.author_use_case.search_authors_by_interests(label)
        return articles, authors[:6]
