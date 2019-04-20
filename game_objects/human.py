import math


from game_objects.game_object import GameObject


class Human():
    def __init__(self, angle: float, planet_x: int, planet_y: int, radius_of_native_planet: int):
        self.x = math.cos(angle) * radius_of_native_planet + planet_x
        self.y = math.sin(angle) * radius_of_native_planet + planet_y
        self.angle = angle
