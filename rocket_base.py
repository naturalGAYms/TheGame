from game_object import GameObject


class RocketBase(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.acceleration = 0.0
        self.angle = 0.0

    def change_angle(self, angle: float):
        pass

    def change_boost(self, moment: float):
        pass
