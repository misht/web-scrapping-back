from typing import Dict, List, Optional, Any, Tuple

from serpapi import GoogleSearch

from src.domain.author.model import DataGraph, ArticleInfo, AuthorInfo, Author, Pagination, Article
from src.domain.user.model import Interest
from src.domain.base import UseCase
from src.domain.base import Error


class AuthorUseCase(UseCase):

    def search_author_id(self, author_id: str):
        params = {
            "engine": "google_scholar_author",
            "author_id": author_id,
            "api_key": "38218a76b3271180ba520332701ad7943bba5a1f07ffd370d5fae6e73de70a88"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        article_info = self.__get_articles_info__(results.get("public_access", {}))
        total_citations = self.__get_total_citations__(results.get("cited_by", {}).get("table"))
        data_graph_list = self.__get_data_graph_list__(results.get("cited_by", {}).get("graph"))
        average = self.__get_average__(data_graph_list)
        articles = self.__get_articles__(results.get("articles", []))
        author = self.__get_author_info__(results.get("author", {}), article_info, total_citations, data_graph_list,
                                          articles, average)
        return author

    def __get_author_info__(self, author: Dict[str, str], article_info: ArticleInfo, total_citations: int,
                            data_graph_list: List[DataGraph], articles: List[Article], average: int) -> AuthorInfo:
        interests = self.__get_interests__(author.get("interests", []))
        return AuthorInfo(name=author.get("name"),
                          affiliations=author.get("affiliations"),
                          interests=interests,
                          picture=author.get("thumbnail"),
                          article_info=article_info,
                          total_citations=total_citations,
                          data_graph_list=data_graph_list,
                          articles=articles,
                          average=average)

    def __get_interests__(self, interest_list: List[Dict]) -> List[Interest]:
        interests = []
        for interest in interest_list:
            interests.append(Interest(title=interest.get("title"),
                                      keyword=interest.get("link").rsplit("label:")[1]))
        return  interests

    def __get_articles_info__(self, public_access: Dict[str, Any]) -> ArticleInfo:
        available = public_access.get("available", 0)
        not_available = public_access.get("not_available", 0)
        total_number_articles = available + not_available
        return ArticleInfo(total_number_articles=total_number_articles,
                           not_available=not_available,
                           available=available)

    def __get_total_citations__(self, table: List[Dict]) -> Optional[int]:
        total_citations = None
        if table:
            total_citations = table[0].get("citations").get("all")
        return total_citations

    def __get_data_graph_list__(self, graph_list: List[Dict[str, int]]) -> List[DataGraph]:
        data_graph_list = []
        if graph_list:
            for graph in graph_list:
                data_graph_list.append(DataGraph(year=graph.get("year"),
                                                 citations=graph.get("citations")))
        return data_graph_list

    def __get_average__(self, data_graph_list: List[DataGraph]) -> int:
        average = 0
        if data_graph_list:
            for data_graph in data_graph_list:
                average += data_graph.citations
            average = round(average / len(data_graph_list))
        return average

    def __get_articles__(self, article_list: List[Dict[str, str]]) -> List[Article]:
        articles = []
        for article in article_list:
            articles.append(Article(title=article.get("title"),
                                    link=article.get("link"),
                                    authors=article.get("authors"),
                                    cited_by=article.get("cited_by", {}).get("value", 0),
                                    year=article.get("year")))
        return articles



    def search_authors_by_interests(self, label: str, next_page: Optional[str],
                                   previous_page: Optional[str]) -> Tuple[List[Author], Pagination]:
        if next_page and previous_page:
            raise Error.bad_request(message="You can only provide next page or previous page",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        params = {
            "engine": "google_scholar_profiles",
            "mauthors": f'label:{label}',
            "api_key": "38218a76b3271180ba520332701ad7943bba5a1f07ffd370d5fae6e73de70a88",
            "after_author": next_page,
            "before_author": previous_page
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        authors = self.__get_authors__(results.get("profiles", []))
        pagination = self.__get_pagination__(results.get("pagination", {}))
        return authors, pagination

    def __get_authors__(self, profiles: List[Dict[str, Any]]) -> List[Author]:
        authors = []
        for profile in profiles:
            interests = self.__get_interests__(profile.get("interests", []))
            authors.append(Author(name=profile.get("name"),
                                  author_id=profile.get("author_id"),
                                  affiliations=profile.get("affiliations"),
                                  cited_by=profile.get("cited_by"),
                                  picture=profile.get("thumbnail"),
                                  interests=interests))
        return authors

    def __get_pagination__(self, pagination: Dict[str, str]) -> Pagination:
        return Pagination(next_page=pagination.get("next_page_token"),
                          previous_page=pagination.get("previous_page_token"))
