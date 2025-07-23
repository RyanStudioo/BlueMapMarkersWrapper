from __future__ import annotations
if annotations:
    from .BaseMarker import BaseMarker

class POIMarker(BaseMarker):
    def __init__(self, key: str, label: str, position:dict, detail:str=None, icon:str=None,
                 anchor: dict=None, classes:list=None):
        super().__init__(key,label, position)
        self.detail = detail
        self.icon = icon
        self.anchor = anchor
        self.classes = classes

    @staticmethod
    def _from_response(response: tuple) -> "POIMarker":
        key = response[0]
        response = response[1]
        label = response['label']
        position = response['position']
        detail = response['detail']
        icon = response['icon']
        anchor = response['anchor']
        classes = response['classes']
        return POIMarker(key, label, position, detail, icon, anchor, classes)