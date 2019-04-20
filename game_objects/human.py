import math

from game_objects.game_object import GameObject


class Human(GameObject):
    def __init__(self, angle: float, radius_of_native_planet: int):
        super().__init__(angle)
        self.x = math.cos(angle) * radius_of_native_planet
        self.y = math.sin(angle) * radius_of_native_planet
        self.angle = angle