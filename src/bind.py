from src.adapters.admin.blueprints import ConfigBlueprint
from src.adapters.admin.repositories import *
from src.adapters.author.blueprints import AuthorBlueprint
from src.adapters.mappers import *
from src.adapters.publication.blueprints import PublicationBlueprint
from src.adapters.user.blueprints import *
from src.adapters.user.repositories import *
from src.domain.admin.usecases import *
from src.domain.author.usecases import *
from src.domain.base import ServiceBind, UseCaseBind, MapperBind
from src.domain.publication.usecases import *
from src.domain.user.usecases import *


class Repositories(RepositoryBind):
    def __init__(self):
        self.user_repository = FirestoreUserRepository()
        self.config_repository = FirestoreConfigRepository()


class Services(ServiceBind):
    def __init__(self):
        self.a = 1


class UseCases(UseCaseBind):
    def __init__(self, repositories: RepositoryBind):
        self.publication_use_case = PublicationUseCase()
        self.author_use_case = AuthorUseCase()
        self.user_use_case = UserUseCase(repositories)
        self.config_use_case = ConfigUseCase(repositories)


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
        self.user_login_mapper = UserLoginMapper()
        self.config_mapper = ConfigMapper()


class Bind:
    def __init__(self):
        repositories = Repositories()
        services = Services()
        use_cases = UseCases(repositories)
        mappers = Mappers()
        self.blueprints = [
            UserBlueprint.create(use_cases, mappers),
            PublicationBlueprint.create(use_cases),
            AuthorBlueprint.create(use_cases, mappers),
            ConfigBlueprint.create(use_cases, mappers)
        ]
