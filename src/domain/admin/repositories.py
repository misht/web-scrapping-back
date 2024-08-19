from abc import abstractmethod

from src.domain.admin.model import Config
from src.domain.base import Repository


class ConfigRepository(Repository):

    @abstractmethod
    def save(self, config: Config) -> Config:
        pass

    @abstractmethod
    def get_by_key(self, config: Config) -> Config:
        pass
