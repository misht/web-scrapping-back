from typing import List

from src.domain.base import Entity


class User(Entity):

    def __init__(self, name: str, email: str, password: str, open_to_collaborate: bool, user_terms_acceptance: bool):
        self.name = name
        self.email = email
        self.password = password
        self.open_to_collaborate = open_to_collaborate
        self.user_terms_acceptance = user_terms_acceptance

    def __repr__(self):
        return ("<User name={}, "
                "email={}, "
                "password={}, "
                "open_to_collaborate={}, "
                "user_terms_acceptance={}>".
                format(self.name,
                       self.email,
                       self.password,
                       self.open_to_collaborate,
                       self.user_terms_acceptance))


class Interest(Entity):
    def __init__(self, title: str, keyword: str):
        self.title = title
        self.keyword = keyword

    def __repr__(self):
        return ("<Interest title={}, "
                "keyword={}>".
                format(self.title,
                       self.keyword))


class SocialNetwork(Entity):

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def __repr__(self):
        return ("<SocialNetwork name={}, "
                "url={}>".
                format(self.name,
                       self.url))


class UserInfo(Entity):

    def __init__(self, name: str, email: str, open_to_collaborate: bool, picture: str = '', affiliation: str = '',
                 schoolar_id: str = '', phone: str = '', interests: List[Interest] = [],
                 social_networks: List[SocialNetwork] = []):
        self.name = name
        self.email = email
        self.open_to_collaborate = open_to_collaborate
        self.picture = picture
        self.affiliation = affiliation
        self.schoolar_id = schoolar_id
        self.phone = phone
        self.interests = interests
        self.social_networks = social_networks

    def __repr__(self):
        return ("<UserInfo name={}, "
                "email={}, "
                "open_to_collaborate={}, "
                "picture={}, "
                "affiliation={}, "
                "schoolar_id={}, "
                "phone={}, "
                "interests={}, "
                "social_networks={}>".
                format(self.name,
                       self.email,
                       self.open_to_collaborate,
                       self.picture,
                       self.affiliation,
                       self.schoolar_id,
                       self.phone,
                       self.interests,
                       self.social_networks))
