from game_objects.game_object import GameObject
from game_objects.planet import Planet
from program_variables import boost_power
import math


class Rocket(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.acceleration = 0.0
        self.angle = 0.0
        self.fuel = 100
        self.boost_power = boost_power
        self.vx = 0
        self.vy = 0

    def change_angle(self, delt_angle: float):
        self.angle += delt_angle

    def enable_boost(self):
        self.vx += self.boost_power * math.cos(self.angle)
        self.vy += self.boost_power * math.sin(self.angle)
        # self.x += self.vx
        # self.y += self.vy

    def move(self):
        self.x += self.vx * math.cos(self.angle)
        self.y += self.vy * math.sin(self.angle)

    # def landing_on_planet(self, closest_planet: Planet):
    #     self.