from __future__ import annotations
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Union, Iterable
import numpy as np

from markers.markers import _get_markers
if annotations:
    from markers.ExtrudeMarker import ExtrudeMarker
    from markers.HTMLMarker import HTMLMarker
    from markers.POIMarker import POIMarker
    from markers.LineMarker import LineMarker
    from markers.ShapeMarker import ShapeMarker

class MarkerSet:
    def __init__(self, key:str, label:str, markers:Iterable):
        self.key = key
        self.label = label
        self.markers = markers

    @staticmethod
    def _from_response(key:str, response_json: dict) -> "MarkerSet":
        label = response_json["label"]
        unformattedMarkers = response_json["markers"]
        markers = []
        start = time.time()
        with ThreadPoolExecutor() as executor:
            markers = executor.map(_get_markers, np.array([i for i in unformattedMarkers.items()]))
        print(time.time() - start)
        return MarkerSet(key, label, markers)

