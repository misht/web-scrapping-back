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