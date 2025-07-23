from __future__ import annotations
from typing import Union
from concurrent.futures import ThreadPoolExecutor
from typing import Iterable
from .markers.markers import get_markers
if annotations:
    pass


class MarkerSet:
    def __init__(self, key:str, label:str, markers:Iterable):
        self.key = key
        self.label = label
        self.markers = markers

    @staticmethod
    def _from_response(key:str, response_json: dict) -> Union["MarkerSet", None]:
        if not response_json: return None
        label = response_json["label"]
        unformattedMarkers = response_json["markers"]
        markers = []
        with ThreadPoolExecutor() as executor:
            markers = executor.map(get_markers, [i for i in unformattedMarkers.items()])
        return MarkerSet(key, label, markers)



