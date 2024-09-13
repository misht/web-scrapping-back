from abc import abstractmethod
from typing import Optional

from src.domain.base import Repository
from src.domain.user.model import User, UserInfo


class UserRepository(Repository):

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        pass


class UserInfoRepository(Repository):

     @abstractmethod
     def save(self, user_info: UserInfo) -> UserInfo:
         pass

     @abstractmethod
     def get_user_by_email(self, email: str) -> Optional[UserInfo]:
        pass
