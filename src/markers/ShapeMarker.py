from __future__ import annotations
if annotations:
    from .BaseMarker import BaseMarker

class ShapeMarker(BaseMarker):
    def __init__(self, key: str, label: str, position: dict, shape:list, shape_y:int, detail:str=None):
        super().__init__(key, label, position)
        self.shape = shape
        self.shape_y = shape_y
        self.detail = detail

    @staticmethod
    def _from_response(response: tuple) -> "ShapeMarker":
        key = response[0]
        response = response[1]
        label = response['label']
        position = response['position']
        shape = response['shape']
        shape_y = response['shapeY']
        detail = response['detail']
        return ShapeMarker(key, label, position, shape, shape_y, detail=detail)