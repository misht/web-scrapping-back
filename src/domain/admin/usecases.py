from src.domain.admin.model import Config
from src.domain.base import Error
from src.domain.base import RepositoryBind
from src.domain.base import UseCase


class ConfigUseCase(UseCase):

    def __init__(self, repositories: RepositoryBind):
        self.config_repository = repositories.config_repository

    def add_config(self, config: Config) -> Config:
        privacy_terms_exist = self.config_repository.get_by_key(config)
        if privacy_terms_exist is not None:
            raise Error.bad_request(message="Config with key {} already exists".format(config.key),
                                    error_code=Error.INVALID_CONFIGURATION_CODE)
        privacy_terms = self.config_repository.save(config)
        return privacy_terms