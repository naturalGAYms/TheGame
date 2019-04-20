from game_objects.game_object import GameObject
from game_objects.planet import Planet
from program_variables import boost_power, mass_of_rocket
import math

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

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

    def change_angle(self, delt_angle: float):
        self.angle += delt_angle

    def enable_boost(self):
        """
        Если корабль на планете то ускорение увеличено
        для того чтобы выбраться за пределы радиуса обнуления вектора движения
        :return:
        """
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
        new_x = self.x + self.vx
        new_y = self.y + self.vy

        # if new_x < 0:
        #     new_x = SCREEN_WIDTH - new_x
        # if new_y < 0:
        #     new_y = SCREEN_HEIGHT - new_y
        #
        # if new_x > SCREEN_WIDTH:
        #     new_x = new_x - SCREEN_WIDTH
        # if new_y > SCREEN_HEIGHT:
        #     new_y = new_y - SCREEN_HEIGHT
        #
        # print(new_x)
        # print(new_y)
        self.x = new_x % SCREEN_WIDTH
        self.y = new_y % SCREEN_HEIGHT

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
