class Position:
    def __init__(self, x:float, y:float, z:float):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def _from_response(response: dict) -> "Position":
        return Position(response['x'], response['y'], response['z'])

class Rotation:
    def __init__(self, pitch:float, roll:float, yaw:float):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

    @staticmethod
    def _from_response(response: dict) -> "Rotation":
        return Rotation(response['pitch'], response['roll'], response['yaw'])