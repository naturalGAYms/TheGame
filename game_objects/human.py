import math

from game_objects.game_object import GameObject


class Human():
    def __init__(self, angle: float, planet_x: int, planet_y: int, radius_of_native_planet: int):
        self.x = planet_x + radius_of_native_planet * math.cos(angle)
        self.y = planet_y + radius_of_native_planet * math.sin(angle)
        self.angle = math.pi + math.atan((self.x - planet_x)/ float(self.y - planet_y))

    def get_coordinates(self):
        return self.x, self.y
