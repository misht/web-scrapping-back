from abc import abstractmethod
from typing import Optional, List

from src.domain.admin.model import Config
from src.domain.base import Repository
from src.domain.user.model import Interest


class ConfigRepository(Repository):

    @abstractmethod
    def save(self, config: Config) -> Config:
        pass

    @abstractmethod
    def get_by_key(self, config: Config) -> Optional[Config]:
        pass


class InterestRepository(Repository):

    @abstractmethod
    def save(self, interest: Interest) -> Interest:
        pass

    @abstractmethod
    def get_by_key(self, interest: Interest) -> Optional[Interest]:
        pass

    @abstractmethod
    def delete_by_key(self, interest: Interest):
        pass

    @abstractmethod
    def list_all(self) -> List[Interest]:
        pass

    @abstractmethod
    def get_by_attribute(self, interest_id: str) -> Optional[Interest]:
        pass
