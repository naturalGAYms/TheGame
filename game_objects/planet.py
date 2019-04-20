from game_objects.game_object import GameObject
from game_objects.human import Human
from program_variables import G
import math


class Planet(GameObject):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius = radius
        self.gravity = G * (math.pi * self.radius * self.radius)

    def get_gravity(self) -> float:
        return self.gravity

    def get_human(self) -> Human:
        pass

    def get_human_angle_coordinate(self) -> float:
        pass