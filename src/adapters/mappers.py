from typing import Dict, Any

from src.domain.author.model import Author, ArticleInfo, DataTable, DataGraph, Interest, Pagination, AuthorInfo
from src.domain.base import Mapper, Error


class BaseMapper(Mapper):

    def from_dict(self, d: Dict):
        try:
            return self.__parse_dict__(d)
        except KeyError as ex:
            raise Error.bad_request(message="Missing required key: {}".format(str(ex)),
                                    error_code=Error.INCOMPLETE_DATA_CODE)

    def __parse_dict__(self, d: Dict):
        return None

    def to_dict(self, o: Any) -> Dict[str, Any]:
        return {}


class ArticleInfoMapper(BaseMapper):

    def to_dict(self, article_info: ArticleInfo) -> Dict[str, int]:
        return {
            "total_number_articles": article_info.total_number_articles,
            "not_available": article_info.not_available,
            "available": article_info.available
        }


class InterestMapper(BaseMapper):

    def to_dict(self, interest: Interest) -> Dict[str, str]:
        return {
            "title": interest.title,
            "keyword": interest.keyword
        }


class DataTableMapper(BaseMapper):

    def to_dict(self, data_table: DataTable) -> Dict[str, int]:
        return {
            "citations": data_table.citations,
            "h_index": data_table.h_index,
            "i10_index": data_table.i10_index
        }


class DataGraphMapper(BaseMapper):

    def to_dict(self, data_graph: DataGraph) -> Dict[str, int]:
        return {
            "year": data_graph.year,
            "citations": data_graph.citations
        }

class AuthorInfoMapper(BaseMapper):

    def __init__(self, article_info_mapper, interest_mapper, data_table_mapper, data_graph_mapper):
        self.article_info_mapper = article_info_mapper
        self.interest_mapper = interest_mapper
        self.data_table_mapper = data_table_mapper
        self.data_graph_mapper = data_graph_mapper

    def to_dict(self, author_info: AuthorInfo) -> Dict[str, Any]:
        return {
            "name": author_info.name,
            "affiliations": author_info.affiliations,
            "interests": [self.interest_mapper.to_dict(interest) for interest in author_info.interests],
            "picture": author_info.picture,
            "articles": self.article_info_mapper.to_dict(author_info.article_info),
            "cited_by": {
                "table": self.data_table_mapper.to_dict(author_info.data_table),
                "graph": [self.data_graph_mapper.to_dict(data_graph) for data_graph in author_info.data_graph_list]
            },
            "open_to_collaborate": author_info.open_to_collaborate
        }


class PaginationMapper(BaseMapper):

    def to_dict(self, pagination: Pagination) -> Dict[str, str]:
        pagination_dict = {}
        if pagination.next_page:
            pagination_dict["next_page"] = pagination.next_page
        if pagination.previous_page:
            pagination_dict["previous_page"] = pagination.previous_page
        return pagination_dict


class AuthorMapper(BaseMapper):

    def __init__(self, interest_mapper, pagination_mapper):
        self.interest_mapper = interest_mapper
        self.pagination_mapper = pagination_mapper

    def to_dict(self, author: Author) -> Dict[str, Any]:
        return {
            "name": author.name,
            "author_id": author.author_id,
            "affiliations": author.affiliations,
            "cited_by": author.cited_by,
            "picture": author.picture,
            "interests": [self.interest_mapper.to_dict(interest) for interest in author.interests],
            "open_to_collaborate": author.open_to_collaborate
        }
