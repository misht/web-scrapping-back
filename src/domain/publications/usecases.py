from src.domain.base import UseCase
from serpapi import GoogleSearch

class PublicationUseCase(UseCase):

    def search_publications(self, query: str, start: int):
        params = {
            "engine": "google_scholar",
            "q": query,
            "api_key": "38218a76b3271180ba520332701ad7943bba5a1f07ffd370d5fae6e73de70a88"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        print(results)
        organic_results = results["organic_results"]
        return organic_results
