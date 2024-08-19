from src.domain.base import Entity
from typing import Any, Optional


class Config(Entity):

    def __init__(self, key: str, value: Optional[Any] = None):
        self.key = key
        self.value = value

    def __repr__(self):
        return ("<Config key={}, "
                "value={}>".
                format(self.key,
                       self.value))