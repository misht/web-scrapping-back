from src.domain.admin.model import Config
from src.domain.base import Error
from src.domain.base import RepositoryBind
from src.domain.base import UseCase
from src.domain.user.model import User
from config import Configuration

class UserUseCase(UseCase):

    def __init__(self, repositories: RepositoryBind):
        self.user_repository = repositories.user_repository
        self.config_repository = repositories.config_repository

    def login(self, email: str, password: str) -> User:
        if not email or not password:
            raise Error.bad_request(message="Missing required keys: name and email",
                                    error_code=Error.INCOMPLETE_DATA_CODE)
        if not type(email) == str or not type(password) == str:
            raise Error.bad_request(message="Data type is invalid.",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        if len(password) < Configuration.MINIMUM_NUMBER_CHARACTERS_FROM_PASSWORD:
            raise Error.bad_request(message="Password should be at least 8 characters.",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        user = User("", email, password, False, True)
        user_exist = self.user_repository.get_user_by_email(user)
        if user_exist is None:
            raise Error.bad_request(message="User with email {} does not exists".format(user.email),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        if user_exist.password != user.password:
            raise Error.bad_request(message="Passwords do not match",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        return user_exist

    def sign_up(self, user: User) -> User:
        user_exist = self.user_repository.get_user_by_email(user)
        if user_exist is not None:
            raise Error.bad_request(message="User {} with email {} already exists".format(user.name, user.email),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        user = self.user_repository.save(user)
        return user

    def get_privacy_terms(self) -> Config:
        privacy_terms = self.config_repository.get_by_key(Config(key='privacy_terms'))
        return privacy_terms

    def get_user_terms(self) -> Config:
        user_terms = self.config_repository.get_by_key(Config(key='user_terms'))
        return user_terms
