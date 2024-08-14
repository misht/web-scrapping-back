from typing import Any

from src.adapters.base import FirestoreRepository
from src.domain.user.model import User
from src.domain.user.repositories import UserRepository


class FirestoreUserRepository(FirestoreRepository, UserRepository):
    def __get_name__(self, user: User) -> str:
        return user.email

    def __object_to_entity__(self, user: User):
        return {"name": user.name,
                "email": user.email,
                "password": user.password}

    def __entity_to_object__(self):
        pass

    def save(self, user: User) -> User:
        self.__save__(user)
        return user

    def __get_kind__(self) -> str:
        return "Users"