from src.adapters.user.blueprints import *
from src.domain.base import RepositoryBind, ServiceBind, UseCaseBind, MapperBind


class Repositories(RepositoryBind):
    def __init__(self):
        self.a = 1


class Services(ServiceBind):
    def __init__(self):
        self.a = 1


class UseCases(UseCaseBind):
    def __init__(self):
        self.a = 1


class Mappers(MapperBind):
    def __init__(self):
        self.a = 1


class Bind:
    def __init__(self):
        repositories = Repositories()
        services = Services()
        use_case = UseCases()
        mappers = Mappers()
        self.blueprints = [
            UserBlueprint.create()
        ]
