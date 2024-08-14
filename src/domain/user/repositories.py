from src.domain.base import Repository
from abc import abstractmethod
from src.domain.user.model import User

class UserRepository(Repository):

    @abstractmethod
    def save(self, user: User) -> User:
        pass