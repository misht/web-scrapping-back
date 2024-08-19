from typing import Dict

from src.adapters.base import FirestoreRepository
from src.domain.admin.model import Config
from src.domain.admin.repositories import ConfigRepository


class FirestoreConfigRepository(FirestoreRepository, ConfigRepository):

    def __get_name__(self, config: Config) -> str:
        return config.key

    def __object_to_entity__(self, config: Config):
        return {"key": config.key,
                "value": config.value}

    def __entity_to_object__(self, entity: Dict[str, any]) -> Config:
        return Config(key=entity["key"],
                      value=entity["value"])

    def save(self, config: Config) -> Config:
        self.__save__(config)
        return config

    def get_by_key(self, config: Config) -> Config:
        config = self.__get_by_name__(config)
        return config

    def __get_kind__(self) -> str:
        return "Config"