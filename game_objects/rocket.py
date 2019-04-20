from game_objects.game_object import GameObject
from game_objects.planet import Planet
from program_variables import boost_power, mass_of_rocket
import math


class Rocket(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.alive = True
        self.on_planet = False
        self.acceleration = 0.0
        self.angle = 0.0
        self.fuel = 100
        self.boost_power = boost_power
        self.mass = mass_of_rocket
        self.vx = 0
        self.vy = 0
        self.fuel = 1010

    def change_angle(self, delt_angle: float):
        self.angle += delt_angle

    def enable_boost(self):
        """
        Если корабль на планете то ускорение увеличено
        для того чтобы выбраться за пределы радиуса обнуления вектора движения
        :return:
        """
        self.fuel -= 1
        if self.fuel < 1:
            return
        self.vx += self.boost_power * math.cos(self.angle)
        self.vy += self.boost_power * math.sin(self.angle)
        if self.on_planet:
            self.on_planet = False
            self.vx += 10 * self.boost_power * math.cos(self.angle)
            self.vy += 10 * self.boost_power * math.sin(self.angle)
        # self.x += self.vx
        # self.y += self.vy

    def return_angle(self):
        return self.angle

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def landing_on_planet(self, closest_planet: Planet):
        """
        Если ракета достаточно близко то вектор движения обнуляется
        :param closest_planet:
        :return:
        """
        if closest_planet.get_distance_to_rocket(self) < closest_planet.radius + 1 and not self.on_planet:
            self.vx = 0
            self.vy = 0
            self.on_planet = True
