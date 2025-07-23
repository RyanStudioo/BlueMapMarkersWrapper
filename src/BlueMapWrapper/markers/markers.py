from __future__ import annotations
from typing import Union

if annotations:
    from ..markers.ExtrudeMarker import ExtrudeMarker
    from ..markers.HTMLMarker import HTMLMarker
    from ..markers.POIMarker import POIMarker
    from ..markers.LineMarker import LineMarker
    from ..markers.ShapeMarker import ShapeMarker

markerTypes = {'poi': POIMarker,
               'html': HTMLMarker,
               'line': LineMarker,
               'shape': ShapeMarker,
               'extrude': ExtrudeMarker}

def get_markers(response:tuple) -> Union[POIMarker, HTMLMarker, LineMarker, ShapeMarker, ExtrudeMarker]:
    key = response[0]
    marker_type = response[1]['type']
    return markerTypes[marker_type]._from_response((key, response[1]))