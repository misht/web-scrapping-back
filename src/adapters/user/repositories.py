from typing import Dict

from src.adapters.base import FirestoreRepository
from src.domain.user.model import User
from src.domain.user.repositories import UserRepository


class FirestoreUserRepository(FirestoreRepository, UserRepository):
    def __get_name__(self, user: User) -> str:
        return user.email

    def __object_to_entity__(self, user: User):
        return {"name": user.name,
                "email": user.email,
                "password": user.password,
                "open_to_collaborate": user.open_to_collaborate}

    def __entity_to_object__(self, entity: Dict[str, any]) -> User:
        return User(name=entity["name"],
                    email=entity["email"],
                    password=entity["password"],
                    open_to_collaborate=entity["open_to_collaborate"])

    def save(self, user: User) -> User:
        self.__save__(user)
        return user

    def get_user_by_email(self, user: User) -> User:
        user = self.__get_by_name__(user)
        return user

    def __get_kind__(self) -> str:
        return "Users"