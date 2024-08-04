from src.adapters.author.blueprints import AuthorBlueprint
from src.adapters.publication.blueprints import PublicationBlueprint
from src.adapters.user.blueprints import *
from src.domain.base import RepositoryBind, ServiceBind, UseCaseBind, MapperBind
from src.domain.publication.usecases import *
from src.domain.author.usecases import *
from src.adapters.mappers import *


class Repositories(RepositoryBind):
    def __init__(self):
        self.a = 1


class Services(ServiceBind):
    def __init__(self):
        self.a = 1


class UseCases(UseCaseBind):
    def __init__(self):
        self.publication_use_case = PublicationUseCase()
        self.author_use_case = AuthorUseCase()


class Mappers(MapperBind):
    def __init__(self):
        self.article_info_mapper = ArticleInfoMapper()
        self.interest_mapper = InterestMapper()
        self.data_table_mapper = DataTableMapper()
        self.data_graph_mapper = DataGraphMapper()
        self.author_mapper = AuthorMapper(self.article_info_mapper, self.interest_mapper, self.data_table_mapper,
                                          self.data_graph_mapper)


class Bind:
    def __init__(self):
        repositories = Repositories()
        services = Services()
        use_cases = UseCases()
        mappers = Mappers()
        self.blueprints = [
            UserBlueprint.create(),
            PublicationBlueprint.create(use_cases),
            AuthorBlueprint.create(use_cases, mappers)
        ]
