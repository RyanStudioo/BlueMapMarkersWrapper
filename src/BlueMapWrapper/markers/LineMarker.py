from __future__ import annotations
if annotations:
    from .BaseMarker import BaseMarker

class LineMarker(BaseMarker):
    def __init__(self, key: str, label: str, position: dict, line:list, detail:str=None):
        super().__init__(key, label, position)
        self.line = line
        self.detail = detail

    @staticmethod
    def _from_response(response: tuple) -> "LineMarker":
        key = response[0]
        response = response[1]
        label = response['label']
        position = response['position']
        line = response['line']
        detail = response['detail']
        return LineMarker(key, label, position, line, detail=detail)