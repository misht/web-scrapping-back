from typing import Dict, List, Optional

from src.domain.base import Entity


class Interest(Entity):
    def __init__(self, title: str, keyword: str):
        self.title = title
        self.keyword = keyword

    def __repr__(self):
        return ("<Interest title={}, "
                "keyword={}>".
                format(self.title,
                       self.keyword))


class ArticleInfo(Entity):
    def __init__(self, total_number_articles: int, not_available: int, available: int):
        self.total_number_articles = total_number_articles
        self.not_available = not_available
        self.available = available

    def __repr__(self):
        return ("<ArticleInfo total_number_articles={}, "
                "not_available={}, "
                "available={}>".
                format(self.total_number_articles,
                       self.not_available,
                       self.available))


class DataTable(Entity):
    def __init__(self, citations: int, h_index: int, i10_index: int):
        self.citations = citations
        self.h_index = h_index
        self.i10_index = i10_index

    def __repr__(self):
        return ("<DataTable citations={}, "
                "h_index={}, "
                "available={}>".
                format(self.citations,
                       self.h_index,
                       self.i10_index))


class DataGraph(Entity):
    def __init__(self, year: int, citations: int):
        self.year = year
        self.citations = citations

    def __repr__(self):
        return ("<DataGraph year={}, "
                "citations={}>".
                format(self.year,
                       self.citations))

class AuthorInfo(Entity):

    def __init__(self, name: str, affiliations: str, interests: List[Interest], picture: str,
                 article_info: ArticleInfo, data_table: DataTable, data_graph_list: List[DataGraph]):
        self.name = name
        self.affiliations = affiliations
        self.interests = interests
        self.picture = picture
        self.article_info = article_info
        self.data_table = data_table
        self.data_graph_list = data_graph_list
        self.open_to_collaborate = True

    def __repr__(self):
        return ("<AuthorInfo name={}, "
                "affiliations={}, "
                "={}, "
                "picture={}, "
                "article_info={},  "
                "data_table={}, "
                "data_graph_list={}, "
                "open_to_collaborate?={}>".
                format(self.name,
                       self.affiliations,
                       self.interests,
                       self.picture,
                       self.article_info,
                       self.data_table,
                       self.data_graph_list,
                       self.open_to_collaborate))

class Author(Entity):

    def __init__(self, name: str, author_id: str, affiliations: str, cited_by: int, picture: str,
                 interests: List[Interest]):
        self.name = name
        self.author_id = author_id
        self.affiliations = affiliations
        self.cited_by = cited_by
        self.picture = picture
        self.interests = interests
        self.open_to_collaborate = False

    def __repr__(self):
        return ("<Author name={}, "
                "author_id={}, "
                "affiliations={}, "
                "cited_by={}, "
                "picture={},  "
                "interests={}, "
                "open_to_collaborate?={}>".
                format(self.name,
                       self.author_id,
                       self.affiliations,
                       self.cited_by,
                       self.picture,
                       self.interests,
                       self.open_to_collaborate))


class Pagination(Entity):
    def __init__(self, next_page: str, previous_page: str):
        self.next_page = next_page
        self.previous_page = previous_page

    def __repr__(self):
        return ("<Pagination next_page={}, "
                "previous_page={}>".
                format(self.next_page,
                       self.previous_page))
