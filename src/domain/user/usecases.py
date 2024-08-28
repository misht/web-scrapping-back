from src.domain.admin.model import Config
from src.domain.base import Error
from src.domain.base import RepositoryBind
from src.domain.base import UseCase
from src.domain.user.model import User, UserInfo


class UserUseCase(UseCase):

    def __init__(self, repositories: RepositoryBind):
        self.user_repository = repositories.user_repository
        self.config_repository = repositories.config_repository
        self.user_info_repository = repositories.user_info_repository

    def login(self, email: str) -> User:
        if not email:
            raise Error.bad_request(message="Missing required keys: email",
                                    error_code=Error.INCOMPLETE_DATA_CODE)
        if not type(email) == str:
            raise Error.bad_request(message="Data type is invalid.",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        user_exist = self.user_repository.get_user_by_email(email)
        if user_exist is None:
            raise Error.bad_request(message="User with email {} does not exists".format(email),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        return user_exist

    def sign_up(self, user: User) -> User:
        user_exist = self.user_repository.get_user_by_email(user.email)
        if user_exist is not None:
            raise Error.bad_request(message="User {} with email {} already exists".format(user.name, user.email),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        user = self.user_repository.save(user)
        user_info =  UserInfo(name=user.name, email=user.email, open_to_collaborate=user.open_to_collaborate)
        self.user_info_repository.save(user_info)
        return user

    def get_privacy_terms(self) -> Config:
        privacy_terms = self.config_repository.get_by_key(Config(key='privacy_terms'))
        return privacy_terms

    def get_user_terms(self) -> Config:
        user_terms = self.config_repository.get_by_key(Config(key='user_terms'))
        return user_terms

    def get_user_info(self, email: str) -> UserInfo:
        if not email:
            raise Error.bad_request(message="Missing required keys: email",
                                    error_code=Error.INCOMPLETE_DATA_CODE)
        if not type(email) == str:
            raise Error.bad_request(message="Data type is invalid.",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        user_info_exist = self.user_info_repository.get_user_by_email(email)
        if user_info_exist is None:
            raise Error.bad_request(message="User info with email does not {} exists.".format(email),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        return user_info_exist

    def edit_user_info(self, user_info: UserInfo) -> UserInfo:
        user_info_exist = self.user_info_repository.get_user_by_email(user_info.email)
        print(f'user_info_exist: {user_info_exist}')
        if user_info_exist is None:
            raise Error.bad_request(message="User with email {} does not exists.".format(user_info.email),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        if user_info_exist.email != user_info.email:
            raise Error.bad_request(message="Email can not be changed.",
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        user_info_exist.name = user_info.name
        user_info_exist.open_to_collaborate = user_info.open_to_collaborate
        user_info_exist.picture = user_info.picture
        user_info_exist.affiliation = user_info.affiliation
        user_info_exist.schoolar_id = user_info.schoolar_id
        user_info_exist.phone = user_info.phone
        user_info_exist.interests = user_info.interests
        user_info_exist.social_networks = user_info.social_networks
        saved_user_info = self.user_info_repository.save(user_info_exist)
        return saved_user_info