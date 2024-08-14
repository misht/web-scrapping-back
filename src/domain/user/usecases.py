from src.domain.base import RepositoryBind
from src.domain.base import UseCase
from src.domain.user.model import User


class UserUseCase(UseCase):

    def __init__(self, repositories: RepositoryBind):
        self.user_repository = repositories.user_repository

    def sign_up(self, user: User) -> User:
        user = self.user_repository.save(user)
        return user
