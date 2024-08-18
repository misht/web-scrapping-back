from src.domain.base import Entity
from typing import List


class User(Entity):

    def __init__(self, name: str, email: str, password: str, open_to_collaborate: bool):
        self.name = name
        self.email = email
        self.password = password
        self.open_to_collaborate = open_to_collaborate

    def __repr__(self):
        return ("<User name={}, "
                "email={}, "
                "password={}, "
                "open_to_collaborate={}>".
                format(self.name,
                       self.email,
                       self.password,
                       self.open_to_collaborate))


class Login(Entity):

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def __repr__(self):
        return ("<Login email={}, "
                "password={}>".
                format(self.email,
                       self.password))