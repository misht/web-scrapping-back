from typing import Dict, Optional, List

from src.adapters.base import FirestoreRepository
from src.domain.admin.model import Config
from src.domain.admin.repositories import ConfigRepository
from src.domain.user.model import Interest


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

    def get_by_key(self, config: Config) -> Optional[Config]:
        config = self.__get_by_name__(config)
        return config

    def __get_kind__(self) -> str:
        return "Config"


class FirestoreInterestRepository(FirestoreRepository, ConfigRepository):

    def __get_name__(self, interest: Interest) -> str:
        return interest.title

    def __object_to_entity__(self, interest: Interest):
        return {"name": interest.title,
                "main_category": interest.main_category,
                "keyword": interest.keyword}

    def __entity_to_object__(self, entity: Dict[str, any]) -> Interest:
        return Interest(title=entity["name"],
                        main_category=entity["main_category"],
                        keyword=entity["keyword"])

    def save(self, interest: Interest) -> Interest:
        self.__save__(interest)
        return interest

    def get_by_key(self, interest: Interest) -> Optional[Interest]:
        interest = self.__get_by_name__(interest)
        return interest

    def get_by_attribute(self, interest_id: str) -> Optional[Interest]:
        interest = self.__get_by_attribute__(interest_id)
        return interest

    def delete_by_key(self, interest: Interest):
        self.__delete_document__(interest)
        return interest

    def list_all(self) -> List[Interest]:
        interests = self.__list_all__()
        return interests

    def __get_kind__(self) -> str:
        return "Interest"
