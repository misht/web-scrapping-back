from typing import Dict, Any

from src.domain.admin.model import Config
from src.domain.author.model import Author, ArticleInfo, DataGraph, Pagination, AuthorInfo, \
    Article
from src.domain.base import Mapper, Error
from src.domain.user.model import User, Interest, UserInfo, SocialNetwork


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

    def __parse_dict__(self, interest_dict: Dict) -> Interest:
        if "title" not in interest_dict or "keyword" not in interest_dict:
            raise Error.bad_request(message="Missing required keys: title and keyword",
                                    error_code=Error.INCOMPLETE_DATA_CODE)
        if not type(interest_dict["title"]) == str or not type(interest_dict["keyword"]) == str:
            raise Error.bad_request(message="Data type is invalid.",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        return Interest(title=interest_dict["title"],
                        keyword=interest_dict["keyword"])
    def to_dict(self, interest: Interest) -> Dict[str, str]:
        return {
            "title": interest.title,
            "keyword": interest.keyword
        }


class DataGraphMapper(BaseMapper):

    def to_dict(self, data_graph: DataGraph) -> Dict[str, int]:
        return {
            "year": data_graph.year,
            "citations": data_graph.citations
        }


class ArticleMapper(BaseMapper):

    def to_dict(self, article: Article) -> Dict[str, int]:
        return {
            "title": article.title,
            "link": article.link,
            "authors": article.authors,
            "cited_by": article.cited_by,
            "year": article.year
        }


class AuthorInfoMapper(BaseMapper):

    def __init__(self, article_info_mapper, interest_mapper, data_graph_mapper, article_mapper):
        self.article_info_mapper = article_info_mapper
        self.interest_mapper = interest_mapper
        self.data_graph_mapper = data_graph_mapper
        self.article_mapper = article_mapper

    def to_dict(self, author_info: AuthorInfo) -> Dict[str, Any]:
        return {
            "name": author_info.name,
            "affiliations": author_info.affiliations,
            "interests": [self.interest_mapper.to_dict(interest) for interest in author_info.interests],
            "picture": author_info.picture,
            "article_info": self.article_info_mapper.to_dict(author_info.article_info),
            "cited_by": {
                "total_citations": author_info.total_citations,
                "graph": [self.data_graph_mapper.to_dict(data_graph) for data_graph in author_info.data_graph_list],
                "average": author_info.average
            },
            "articles": [self.article_mapper.to_dict(article) for article in author_info.articles],
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


class UserMapper(BaseMapper):

    def __parse_dict__(self, user_dict: Dict) -> User:
        if "name" not in user_dict or "email" not in user_dict \
            or "password" not in user_dict or "open_to_collaborate" not in user_dict \
                or "user_terms_acceptance" not in user_dict:
            raise Error.bad_request(message="Missing required keys: name, email, password, "
                                            "open_to_collaborate and user_terms_acceptance",
                                    error_code=Error.INCOMPLETE_DATA_CODE)
        if not type(user_dict["name"]) == str or not type(user_dict["email"]) == str \
            or not type(user_dict["password"]) == str or not type(user_dict["open_to_collaborate"]) == bool \
                or not type(user_dict["user_terms_acceptance"]) == bool:
            raise Error.bad_request(message="Data type is invalid.",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        return User(name=user_dict["name"],
                    email=user_dict["email"],
                    password=user_dict["password"],
                    open_to_collaborate=user_dict["open_to_collaborate"],
                    user_terms_acceptance=user_dict["user_terms_acceptance"])

    def to_dict(self, user: User) -> Dict[str, Any]:
        return {"name": user.name,
                "email": user.email,
                "password": user.password}


class SocialNetworkMapper(BaseMapper):

    def __parse_dict__(self, social_network_dict: Dict) -> SocialNetwork:
        if "name" not in social_network_dict or "url" not in social_network_dict:
            raise Error.bad_request(message="Missing required keys: title and keyword",
                                    error_code=Error.INCOMPLETE_DATA_CODE)
        if not type(social_network_dict["name"]) == str or not type(social_network_dict["url"]) == str:
            raise Error.bad_request(message="Data type is invalid.",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        return SocialNetwork(name=social_network_dict["name"],
                             url=social_network_dict["url"])

    def to_dict(self, social_network: SocialNetwork) -> Dict[str, str]:
        return {
            "name": social_network.name,
            "url": social_network.url
        }


class UserInfoMapper(BaseMapper):

    def __init__(self, interest_mapper, social_network_mapper):
        self.interest_mapper = interest_mapper
        self.social_network_mapper = social_network_mapper

    def __parse_dict__(self, user_info_dict: Dict) -> UserInfo:
        if "name" not in user_info_dict or "email" not in user_info_dict \
                or "open_to_collaborate" not in user_info_dict or "picture" not in user_info_dict \
                or "affiliation" not in user_info_dict or "schoolar_id" not in user_info_dict \
                or "phone" not in user_info_dict or "interests" not in user_info_dict \
                or "ssnn" not in user_info_dict:
            raise Error.bad_request(message="Missing required keys: name, email, open_to_collaborate, picture, "
                                            "affiliation, schoolar_id, phone, interests and ssnn.",
                                    error_code=Error.INCOMPLETE_DATA_CODE)
        if not type(user_info_dict["name"]) == str or not type(user_info_dict["email"]) == str \
                or not type(user_info_dict["open_to_collaborate"]) == bool \
                or not type(user_info_dict["picture"]) == str or not type(user_info_dict["affiliation"]) == str \
                or not type(user_info_dict["schoolar_id"]) == str or not type(user_info_dict["phone"]) == str \
                or not type(user_info_dict["interests"]) == list or not type(user_info_dict["ssnn"]) == list:
            raise Error.bad_request(message="Data type is invalid.",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        return UserInfo(name=user_info_dict["name"],
                        email=user_info_dict["email"],
                        open_to_collaborate=user_info_dict["open_to_collaborate"],
                        picture=user_info_dict["picture"],
                        affiliation=user_info_dict["affiliation"],
                        schoolar_id=user_info_dict["schoolar_id"],
                        phone=user_info_dict["phone"],
                        interests=[self.interest_mapper.from_dict(interest)
                                   for interest in user_info_dict["interests"]],
                        social_networks=[self.social_network_mapper.from_dict(sn)
                                         for sn in user_info_dict["ssnn"]])

    def to_dict(self, user_info: UserInfo) -> Dict[str, Any]:
        return {
            "name": user_info.name,
            "email": user_info.email,
            "open_to_collaborate": user_info.open_to_collaborate,
            "picture": user_info.picture,
            "affiliation": user_info.affiliation,
            "schoolar_id": user_info.schoolar_id,
            "phone": user_info.phone,
            "interests": [self.interest_mapper.to_dict(interest) for interest in user_info.interests],
            "ssnn": [self.social_network_mapper.to_dict(social_network) for social_network in user_info.social_networks]
        }


class ConfigMapper(BaseMapper):

    def __parse_dict__(self, config_dict: Dict) -> Config:
        if "key" not in config_dict or "value" not in config_dict:
            raise Error.bad_request(message="Missing required keys: key and value",
                                    error_code=Error.INCOMPLETE_DATA_CODE)
        if not type(config_dict["key"]) == str or not type(config_dict["value"]) == str:
            raise Error.bad_request(message="Data type is invalid.",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        return Config(key=config_dict["key"],
                      value=config_dict["value"])

    def to_dict(self, config: Config) -> Dict[str, str]:
        return {
            "value": config.value
        }


class InterestAdminMapper(BaseMapper):

    def __parse_dict__(self, interest_admin_dict: Dict) -> Interest:
        if "name" not in interest_admin_dict or "keyword" not in interest_admin_dict \
                or "main_category" not in interest_admin_dict:
            raise Error.bad_request(message="Missing required keys: name, keyword and main_category",
                                    error_code=Error.INCOMPLETE_DATA_CODE)
        if not type(interest_admin_dict["name"]) == str or not type(interest_admin_dict["keyword"]) == str \
                or not type(interest_admin_dict["main_category"]) == str:
            raise Error.bad_request(message="Data type is invalid.",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        return Interest(title=interest_admin_dict["name"],
                        keyword=interest_admin_dict["keyword"],
                        main_category=interest_admin_dict["main_category"])
    def to_dict(self, interest: Interest) -> Dict[str, str]:
        return {
            "title": interest.title,
            "keyword": interest.keyword,
            "main_category": interest.main_category
        }