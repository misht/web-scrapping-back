from abc import abstractmethod

from src.domain.admin.model import Config
from src.domain.base import Repository
from src.domain.user.model import Interest


class ConfigRepository(Repository):

    @abstractmethod
    def save(self, config: Config) -> Config:
        pass

    @abstractmethod
    def get_by_key(self, config: Config) -> Config:
        pass


class InterestRepository(Repository):

    @abstractmethod
    def save(self, interest: Interest) -> Interest:
        pass

    @abstractmethod
    def get_by_key(self, interest: Interest) -> Interest:
        pass

    @abstractmethod
    def delete_by_key(self, interest: Interest):
        pass
