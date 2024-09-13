from src.adapters.admin.blueprints import ConfigBlueprint
from src.adapters.admin.repositories import *
from src.adapters.author.blueprints import AuthorBlueprint
from src.adapters.mappers import *
from src.adapters.article.blueprints import ArticleBlueprint
from src.adapters.user.blueprints import *
from src.adapters.user.repositories import *
from src.domain.admin.usecases import *
from src.domain.author.usecases import *
from src.domain.base import ServiceBind, UseCaseBind, MapperBind
from src.domain.article.usecases import *
from src.domain.user.usecases import *


class Repositories(RepositoryBind):
    def __init__(self):
        self.user_repository = FirestoreUserRepository()
        self.config_repository = FirestoreConfigRepository()
        self.user_info_repository = FirestoreUserInfoRepository()
        self.interest_repository = FirestoreInterestRepository()


class Services(ServiceBind):
    def __init__(self):
        self.a = 1


class UseCases(UseCaseBind):
    def __init__(self, repositories: RepositoryBind):
        self.author_use_case = AuthorUseCase()
        self.user_use_case = UserUseCase(repositories)
        self.config_use_case = ConfigUseCase(repositories)
        self.interest_use_case = InterestUseCase(repositories)
        self.article_use_case = ArticleUseCase(self.author_use_case)


class Mappers(MapperBind):
    def __init__(self):
        self.article_info_mapper = ArticleInfoMapper()
        self.interest_mapper = InterestMapper()
        self.data_graph_mapper = DataGraphMapper()
        self.article_mapper = ArticleMapper()
        self.author_info_mapper = AuthorInfoMapper(self.article_info_mapper, self.interest_mapper,
                                                   self.data_graph_mapper, self.article_mapper)
        self.pagination_mapper = PaginationMapper()
        self.author_mapper = AuthorMapper(self.interest_mapper, self.pagination_mapper)
        self.user_mapper = UserMapper()
        self.config_mapper = ConfigMapper()
        self.social_network_mapper = SocialNetworkMapper()
        self.interest_admin_mapper = InterestAdminMapper()
        self.user_info_mapper = UserInfoMapper(self.interest_admin_mapper, self.social_network_mapper)
        self.user_interest_mapper = UserInterestMapper(self.interest_mapper)
        self.second_article_mapper = SecondArticleMapper()
        self.interests_mapper = InterestsMapper(self.interest_admin_mapper)


class Bind:
    def __init__(self):
        repositories = Repositories()
        services = Services()
        use_cases = UseCases(repositories)
        mappers = Mappers()
        self.blueprints = [
            UserBlueprint.create(use_cases, mappers),
            ArticleBlueprint.create(use_cases, mappers),
            AuthorBlueprint.create(use_cases, mappers),
            ConfigBlueprint.create(use_cases, mappers)
        ]
