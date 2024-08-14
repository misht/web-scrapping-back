from src.domain.base import Entity
from typing import List


class User(Entity):

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return ("<User name={}, "
                "email={}, "
                "password={}>".
                format(self.name,
                       self.email,
                       self.password))