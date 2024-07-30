from abc import ABCMeta, abstractmethod
from typing import Dict, Any


class RepositoryBind(metaclass=ABCMeta):
    pass


class ServiceBind(metaclass=ABCMeta):
    pass


class UseCaseBind(metaclass=ABCMeta):
    pass


class MapperBind(metaclass=ABCMeta):
    pass


class Blueprint(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create(*args):
        pass


class Entity(metaclass=ABCMeta):
    pass


class UseCase(metaclass=ABCMeta):
    pass


class Service(metaclass=ABCMeta):
    pass


class Repository(metaclass=ABCMeta):
    pass


class Mapper(metaclass=ABCMeta):
    @abstractmethod
    def from_dict(self, d: Dict) -> Any:
        pass

    @abstractmethod
    def to_dict(self, d: Any) -> Dict:
        pass


class Error(Exception):

    UNAUTHORIZED_CODE = "UNAUTHORIZED"
    INVALID_CONFIGURATION_CODE = "INVALID_CONFIGURATION"
    INCOMPLETE_DATA_CODE = "INCOMPLETE_DATA"
    INTERNAL_ERROR_CODE = "INTERNAL_ERROR"
    NOT_FOUND_CODE = "NOT_FOUND"

    def __init__(self, code: int, message: str, error_code: str):
        super(Error).__init__(message)
        self.code = code
        self.message = message
        self.error_code = error_code


    @classmethod
    def bad_request(cls, *, error_code: str, message: str = 'Bad request'):
        return Error(400, message, error_code, message)

    @classmethod
    def unauthorized(cls, *, error_code: str, message: str = 'Unauthorized'):
        return Error(401, message, error_code, message)

    @classmethod
    def invalid_configuration(cls, *, error_code: str = INVALID_CONFIGURATION_CODE,
                              message: str = 'Invalid configuration'):
        return Error(500, message, error_code, message)

    @classmethod
    def not_found(cls, *, error_code: str =  NOT_FOUND_CODE, message: str = 'Not found'):
        return Error(404, message, error_code, message)
