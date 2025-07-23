from .coordinates import Position, Rotation

class Player:
    def __init__(self, uuid:str, name:str, foreign:bool, position:Position, rotation:Rotation):
        self.uuid = uuid
        self.name = name
        self.foreign = foreign
        self.position = position
        self.rotation = rotation

    @staticmethod
    def _from_response(response: dict) -> "Player":
        if not response: return None
        return Player(response['uuid'], response['name'], response['foreign'],
                      Position._from_response(response['position']),
                      Rotation._from_response(response['rotation']))