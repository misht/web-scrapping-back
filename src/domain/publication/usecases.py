from typing import Dict, List

from serpapi import GoogleSearch

from src.domain.base import UseCase
from src.domain.publication.model import Author, Publication


class PublicationUseCase(UseCase):

    def search_publications(self, query: str, start: int):
        params = {
            "engine": "google_scholar",
            "q": query,
            "api_key": "38218a76b3271180ba520332701ad7943bba5a1f07ffd370d5fae6e73de70a88",
            "start": start
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        print(results)
        total_results = self.__get_total_results__(results.get("search_information", {}))
        authors = self.__get_authors__(results.get("profiles", {}))
        results = results.get("organic_results")
        publications = self.__get_publications__(results.get("serpapi_pagination", {}), start, total_results)
        return results

    def __get_total_results__(self, search_information: Dict) -> int:
        total_results = search_information.get("total_results", 0)
        return total_results

    def __get_authors__(self, profiles: Dict) -> List[Author]:
        authors = []
        author_list = profiles.get("author", [])
        if author_list:
            for author in author_list:
                authors.append(Author(name=author.get("name"),
                                      author_id=author.get("author_id")))
        return authors

    def __get_results__(self):
        pass

    def __get_publications__(self, pagination: Dict, start: int, total_results: int) -> List[Publication]:
        publication_list = []
        current_page = pagination.get("current_page")
        pagination = pagination.get("other_pages", {})
        if pagination:
            previous_page = pagination.get(str(current_page - 1), start)
            next_page = pagination.get(str(current_page + 1))
            publication_list.append(Publication(current_page=current_page,
                                                previous_page=previous_page.rsplit("&start=")[1],
                                                next_page=next_page.rsplit("&start=")[1],
                                                total_results=total_results))
        return publication_list