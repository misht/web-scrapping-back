from typing import Dict, Any

from src.domain.base import Mapper, Error


class BaseMapper(Mapper):

    def from_dict(self, d: Dict):
        try:
            return self.__parse_dict__(d)
        except KeyError as ex:
            raise Error.bad_request(message="Missing required key: {}".format(str(ex)),
                                    error_code=Error.INCOMPLETE_DATA_CODE)

    def __parse_dict__(self, d: Dict):
        return None

    def to_dict(self, o: Any):
        return {}


class PublicationMapper(BaseMapper):

    def to_dict(self, o: Any):
        return o.to_dict()