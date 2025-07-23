from __future__ import annotations
from typing import Union

if annotations:
    from src.BlueMapWrapper.markers.ExtrudeMarker import ExtrudeMarker
    from src.BlueMapWrapper.markers.HTMLMarker import HTMLMarker
    from src.BlueMapWrapper.markers.POIMarker import POIMarker
    from src.BlueMapWrapper.markers.LineMarker import LineMarker
    from src.BlueMapWrapper.markers.ShapeMarker import ShapeMarker

markerTypes = {'poi': POIMarker,
               'html': HTMLMarker,
               'line': LineMarker,
               'shape': ShapeMarker,
               'extrude': ExtrudeMarker}

def _get_markers(response:tuple) -> Union[POIMarker, HTMLMarker, LineMarker, ShapeMarker, ExtrudeMarker]:
    key = response[0]
    marker_type = response[1]['type']
    return markerTypes[marker_type]._from_response(response)