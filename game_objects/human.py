import math

from game_objects.game_object import GameObject


class Human():
    def __init__(self, angle: float, radius_of_native_planet: int):
        # super().__init__(angle, 0)
        self.x = math.cos(angle) * radius_of_native_planet
        self.y = math.sin(angle) * radius_of_native_planet
        self.angle = angle
