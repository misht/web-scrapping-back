from src.domain.base import Entity
from typing import Optional

class Publication(Entity):

    def __init__(self, current_page: int, next_page: int, previous_page: int, total_results: int):
        self.current_page = current_page
        self.previous_page = previous_page
        self.next_page = next_page
        self.total_results = total_results
        self.profiles = []
        self.results = []


class Profile(Entity):

    def __init__(self, title: str):
        self.title = title
        self.authors = []


class Author(Entity):

    def __init__(self, name: str, author_id: str, title: Optional[str] = "", snippet: Optional[str] = ""):
        self.name = name
        self.author_id = author_id
        self.title = title
        self.snippet = snippet
