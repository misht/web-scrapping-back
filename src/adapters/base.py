from abc import ABCMeta, abstractmethod
from firebase_admin import firestore
from typing import Any

class FirestoreRepository(metaclass=ABCMeta):

    def __init__(self):
        self.client = firestore.client()

    @abstractmethod
    def __get_kind__(self) -> str:
        pass

    @abstractmethod
    def __get_name__(self, obj: Any) -> str:
        pass

    @abstractmethod
    def __object_to_entity__(self, obj: Any):
        pass

    @abstractmethod
    def __entity_to_object__(self):
        pass

    def __save__(self, obj: Any):
        doc_ref = self.client.collection(self.__get_kind__()).document(self.__get_name__(obj))
        doc_ref.set(self.__object_to_entity__(obj))

    def __get_by_name__(self, obj: Any, name: str):
        doc_ref = self.client.collection(self.__get_kind__()).document(self.__get_name__(obj))
        doc_ref.get()