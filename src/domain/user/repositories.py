from abc import abstractmethod

from src.domain.base import Repository
from src.domain.user.model import User


class UserRepository(Repository):

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user_by_email(self, user: User) -> User:
        pass
