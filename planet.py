from game_object import GameObject
from human import Human


class Planet(GameObject):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius = radius

    def get_gravity(self) -> float:
        # TODO какая-то физика, которая зависит от радиуса планеты
        pass

    def get_human(self) -> Human:
        pass

    def get_human_angle_coordinate(self) -> float:
        pass
