from __future__ import annotations
from typing import Union

if annotations:
    from src.markers.ExtrudeMarker import ExtrudeMarker
    from src.markers.HTMLMarker import HTMLMarker
    from src.markers.POIMarker import POIMarker
    from src.markers.LineMarker import LineMarker
    from src.markers.ShapeMarker import ShapeMarker

markerTypes = {'poi': POIMarker,
               'html': HTMLMarker,
               'line': LineMarker,
               'shape': ShapeMarker,
               'extrude': ExtrudeMarker}

def _get_markers(response:tuple) -> Union[POIMarker, HTMLMarker, LineMarker, ShapeMarker, ExtrudeMarker]:
    key = response[0]
    marker_type = response[1]['type']
    return markerTypes[marker_type]._from_response(response)