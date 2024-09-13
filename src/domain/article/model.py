from src.domain.base import Entity


class Article(Entity):

    def __init__(self, authors: str, cited_by: int, link: str, title: str, snippet: str):
        self.authors = authors
        self.cited_by = cited_by
        self.link = link
        self.title = title
        self.snippet = snippet

    def __repr__(self):
        return ("<Article authors={}, "
                "cited_by={}, "
                "link={}, "
                "title={}, "
                "snippet={}>".
                format(self.authors,
                       self.cited_by,
                       self.link,
                       self.title,
                       self.snippet))
