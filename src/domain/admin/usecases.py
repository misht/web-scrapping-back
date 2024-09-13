from src.domain.admin.model import Config
from src.domain.base import Error
from src.domain.base import RepositoryBind
from src.domain.base import UseCase
from src.domain.user.model import Interest


class ConfigUseCase(UseCase):

    def __init__(self, repositories: RepositoryBind):
        self.config_repository = repositories.config_repository

    def add_config(self, config: Config) -> Config:
        privacy_terms_exist = self.config_repository.get_by_key(config)
        if privacy_terms_exist is not None:
            raise Error.bad_request(message="Config with key {} already exists.".format(config.key),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        saved_privacy_terms = self.config_repository.save(config)
        return saved_privacy_terms


class InterestUseCase(UseCase):

    def __init__(self, repositories: RepositoryBind):
        self.interest_repository = repositories.interest_repository

    def add_interest(self, interest: Interest) -> Interest:
        exist_interest = self.interest_repository.get_by_key(interest)
        if exist_interest is not None:
            raise Error.bad_request(message="Interest with name {} already exists.".format(interest.title),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        saved_interest = self.interest_repository.save(interest)
        return saved_interest

    def edit_interest(self, interest: Interest) -> Interest:
        exist_interest = self.interest_repository.get_by_key(interest)
        if exist_interest is None:
            raise Error.bad_request(message="Interest with name {} does not exist.".format(interest.title),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        if exist_interest.title != interest.title:
            raise Error.bad_request(message="Interest name can not be changed.".format(interest.title),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        exist_interest.keyword = interest.keyword
        exist_interest.main_category = interest.main_category
        saved_interest = self.interest_repository.save(exist_interest)
        return saved_interest

    def delete_interest(self, interest_id: str) -> Interest:
        exist_interest = self.interest_repository.get_by_attribute(interest_id)
        if exist_interest is None:
            raise Error.bad_request(message="Interest with name {} does not exist.".format(interest_id),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        self.interest_repository.delete_by_key(exist_interest)
        return exist_interest