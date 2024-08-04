from typing import Dict, List, Optional, Any

from serpapi import GoogleSearch

from src.domain.author.model import DataTable, DataGraph, ArticleInfo, Author, Interest
from src.domain.base import UseCase


class AuthorUseCase(UseCase):

    def search_author_id(self, author_id: str):
        params = {
            "engine": "google_scholar_author",
            "author_id": author_id,
            "api_key": "38218a76b3271180ba520332701ad7943bba5a1f07ffd370d5fae6e73de70a88"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        article_info = self.__get_articles_info(results.get("public_access"))
        data_table = self.__get_data_table__(results.get("cited_by").get("table"))
        data_graph_list = self.__get_data_graph_list__(results.get("cited_by").get("graph"))
        author = self.__get_author__(results.get("author"), article_info, data_table, data_graph_list)
        print(results)
        return author

    def __get_author__(self, author: Dict[str, str], article_info: ArticleInfo, data_table: DataTable,
                       data_graph_list: List[DataGraph]) -> Author:
        interests = self.__get_interests__(author.get("interests", []))
        return Author(name=author.get("name"),
                      affiliations=author.get("affiliations"),
                      interests=interests,
                      picture=author.get("thumbnail"),
                      article_info=article_info,
                      data_table=data_table,
                      data_graph_list=data_graph_list)

    def __get_interests__(self, interest_list: List[Dict]) -> List[Interest]:
        interests = []
        for interest in interest_list:
            interests.append(Interest(title=interest.get("title"),
                                      keyword=interest.get("link").rsplit("label:")[1]))
        return  interests

    def __get_articles_info(self, public_access: Dict[str, Any]) -> ArticleInfo:
        available = public_access.get("available", 0)
        not_available = public_access.get("not_available", 0)
        total_number_articles = available +  not_available
        return ArticleInfo(total_number_articles=total_number_articles,
                           not_available=available,
                           available=not_available)

    def __get_data_table__(self, table: List[Dict]) -> Optional[DataTable]:
        data_table = None
        if table:
            data_table = DataTable(citations=table[0].get("citations").get("all"),
                                   h_index=table[1].get("h_index").get("all"),
                                   i10_index=table[2].get("i10_index").get("all"))
        return data_table

    def __get_data_graph_list__(self, graph_list: List[Dict[str, int]]) -> List[DataGraph]:
        data_graph_list = []
        if graph_list:
            for graph in graph_list:
                data_graph_list.append(DataGraph(year=graph.get("year"),
                                                 citations=graph.get("citations")))
        return data_graph_list