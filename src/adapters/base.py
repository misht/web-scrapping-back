from abc import ABCMeta, abstractmethod
from typing import Any, Dict

from firebase_admin import firestore


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
    def __entity_to_object__(self, entity: Dict[str, any]):
        pass

    def __save__(self, obj: Any):
        doc_ref = self.client.collection(self.__get_kind__()).document(self.__get_name__(obj))
        doc_ref.set(self.__object_to_entity__(obj))

    def __get_by_name__(self, obj: Any):
        doc_ref = self.client.collection(self.__get_kind__()).document(self.__get_name__(obj))
        doc = doc_ref.get()
        return self.__entity_to_object__(doc.to_dict()) if doc.exists else None

    def __get_by_attribute__(self, attribute: Any):
        doc_ref = self.client.collection(self.__get_kind__()).document(attribute)
        doc = doc_ref.get()
        return self.__entity_to_object__(doc.to_dict()) if doc.exists else None

    def __delete_document__(self, obj: Any):
        doc_ref = self.client.collection(self.__get_kind__()).document(self.__get_name__(obj)).delete()