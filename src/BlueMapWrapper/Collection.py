from typing import Union

from .MarkerSet import MarkerSet


class Collection:
    def __init__(self, marker_sets: list[MarkerSet]):
        self.marker_sets = marker_sets

    @staticmethod
    def _from_response(response: dict) -> "Collection":
        return Collection([MarkerSet._from_response(key, item) for key, item in response.items()])

    def from_key(self, key:str) -> Union[MarkerSet, None]:
        matches = [i for i in self.marker_sets if i.key == key]
        if not matches:
            return None
        if len(matches) > 1:
            raise KeyError(f"Multiple Keys found for '{key}'")
        return matches[0]