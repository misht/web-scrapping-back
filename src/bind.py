from src.adapters.publications.blueprints import PublicationBlueprint
from src.adapters.user.blueprints import *
from src.domain.base import RepositoryBind, ServiceBind, UseCaseBind, MapperBind
from src.domain.publications.usecases import PublicationUseCase


class Repositories(RepositoryBind):
    def __init__(self):
        self.a = 1


class Services(ServiceBind):
    def __init__(self):
        self.a = 1


class UseCases(UseCaseBind):
    def __init__(self):
        self.publication_use_case = PublicationUseCase()


class Mappers(MapperBind):
    def __init__(self):
        self.a = 1


class Bind:
    def __init__(self):
        repositories = Repositories()
        services = Services()
        use_cases = UseCases()
        mappers = Mappers()
        self.blueprints = [
            UserBlueprint.create(),
            PublicationBlueprint.create(use_cases)
        ]
