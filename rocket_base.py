class RocketBase:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.acceleration = 0.0
        self.angle = 0.0

    def get_coordinates(self) -> (int, int):
        pass

    def change_angle(self, angle: float):
        pass

    def change_boost(self, moment: float):
        pass
