from typing import Union
from .MarkerSet import MarkerSet
from .player import Player
from .exceptions import NoMatches, MultipleMatches


class MarkerCollection:
    def __init__(self, marker_sets: list[MarkerSet]):
        self.marker_sets = marker_sets

    @staticmethod
    def _from_response(response: dict) -> Union["MarkerCollection", None]:
        return MarkerCollection([MarkerSet._from_response(key, item) for key, item in response.items()])

    def from_key(self, key:str) -> Union[MarkerSet, None]:
        matches = [i for i in self.marker_sets if i.key == key]
        if not matches:
            return None
        if len(matches) > 1:
            raise MultipleMatches(key)
        return matches[0]

class PlayerCollection:
    def __init__(self, players: list[Player]):
        self.players = players

    @staticmethod
    def _from_response(response: dict) -> Union["PlayerCollection", None]:
        players = response['players']
        return PlayerCollection([Player._from_response(item) for item in players])

    def from_uuid(self, uuid:str) -> Union[Player, None]:
        matches = [i for i in self.players if i.uuid == uuid]
        if not matches:
            return None
        if len(matches) > 1:
            raise MultipleMatches(uuid)
        return matches[0]

    def from_name(self, name:str) -> Union[Player, None]:
        matches = [i for i in self.players if i.name.lower() == name.lower()]
        if not matches:
            return None
        if len(matches) > 1:
            raise MultipleMatches(name)
        return matches[0]

class Collection:
    def __init__(self, marker_collection: MarkerCollection, player_collection: PlayerCollection):
        self.marker_collection = marker_collection
        self.player_collection = player_collection

    @staticmethod
    def _from_response(marker_response: dict, player_response: dict) -> "Collection":
        marker_collection = MarkerCollection._from_response(marker_response)
        player_collection = PlayerCollection._from_response(player_response)
        return Collection(marker_collection, player_collection)