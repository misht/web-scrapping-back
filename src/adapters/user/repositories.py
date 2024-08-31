from typing import Dict, Optional

from src.adapters.base import FirestoreRepository
from src.domain.user.model import User, UserInfo, Interest, SocialNetwork
from src.domain.user.repositories import UserRepository, UserInfoRepository


class FirestoreUserRepository(FirestoreRepository, UserRepository):

    def __get_name__(self, user: User) -> str:
        return user.email

    def __object_to_entity__(self, user: User):
        return {"name": user.name,
                "email": user.email,
                "password": user.password,
                "open_to_collaborate": user.open_to_collaborate,
                "user_terms_acceptance": user.user_terms_acceptance}

    def __entity_to_object__(self, entity: Dict[str, any]) -> User:
        return User(name=entity["name"],
                    email=entity["email"],
                    password=entity["password"],
                    open_to_collaborate=entity["open_to_collaborate"],
                    user_terms_acceptance=entity.get("user_terms_acceptance", True))

    def save(self, user: User) -> User:
        self.__save__(user)
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        user = self.__get_by_attribute__(email)
        return user

    def __get_kind__(self) -> str:
        return "User"


class FirestoreUserInfoRepository(FirestoreRepository, UserInfoRepository):

    def __get_name__(self, user_info: UserInfo) -> str:
        return user_info.email

    def __object_to_entity__(self, user_info: UserInfo):
        return {"name": user_info.name,
                "email": user_info.email,
                "open_to_collaborate": user_info.open_to_collaborate,
                "picture": user_info.picture,
                "affiliation": user_info.affiliation,
                "schoolar_id": user_info.schoolar_id,
                "phone": user_info.phone,
                "interests": [interest.to_dict() for interest in user_info.interests],
                "social_networks": [sn.to_dict() for sn in user_info.social_networks]
                }

    def __entity_to_object__(self, entity: Dict[str, any]) -> UserInfo:
        return UserInfo(name=entity["name"],
                        email=entity["email"],
                        open_to_collaborate=entity["open_to_collaborate"],
                        picture=entity["picture"],
                        affiliation=entity["affiliation"],
                        schoolar_id=entity["schoolar_id"],
                        phone=entity["phone"],
                        interests=[Interest(interest.get("title"), interest.get("keyword"),
                                            interest.get("main_category"))
                                   for interest in entity["interests"]],
                        social_networks=[SocialNetwork(sn.get("name"), sn.get("url"))
                                         for sn in entity["social_networks"]])

    def save(self, user_info: UserInfo) -> UserInfo:
        self.__save__(user_info)
        return user_info

    def get_user_by_email(self, email: str) -> Optional[UserInfo]:
        user_info = self.__get_by_attribute__(email)
        return user_info

    def __get_kind__(self) -> str:
        return "UserInfo"
