from src.adapters.author.blueprints import AuthorBlueprint
from src.adapters.publication.blueprints import PublicationBlueprint
from src.adapters.user.blueprints import *
from src.domain.base import RepositoryBind, ServiceBind, UseCaseBind, MapperBind
from src.domain.publication.usecases import *
from src.domain.author.usecases import *
from src.adapters.mappers import *
from src.adapters.user.repositories import *
from src.domain.user.usecases import UserUseCase


class Repositories(RepositoryBind):
    def __init__(self):
        self.user_repository = FirestoreUserRepository()


class Services(ServiceBind):
    def __init__(self):
        self.a = 1


class UseCases(UseCaseBind):
    def __init__(self, repositories: RepositoryBind):
        self.publication_use_case = PublicationUseCase()
        self.author_use_case = AuthorUseCase()
        self.user_use_case = UserUseCase(repositories)


class Mappers(MapperBind):
    def __init__(self):
        self.article_info_mapper = ArticleInfoMapper()
        self.interest_mapper = InterestMapper()
        self.data_table_mapper = DataTableMapper()
        self.data_graph_mapper = DataGraphMapper()
        self.author_mapper = AuthorMapper(self.article_info_mapper, self.interest_mapper, self.data_table_mapper,
                                          self.data_graph_mapper)
        self.user_mapper = UserMapper()
        self.user_login_mapper = UserLoginMapper()


class Bind:
    def __init__(self):
        repositories = Repositories()
        services = Services()
        use_cases = UseCases(repositories)
        mappers = Mappers()
        self.blueprints = [
            UserBlueprint.create(use_cases, mappers),
            PublicationBlueprint.create(use_cases),
            AuthorBlueprint.create(use_cases, mappers)
        ]
