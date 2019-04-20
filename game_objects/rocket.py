from game_objects.game_object import GameObject
from game_objects.planet import Planet
from program_variables import boost_power, mass_of_rocket
from process_logic import get_distance
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

    def collision_with_planet(self, closest_planet: Planet):
        """
        Если ракета достаточно близко то вектор движения обнуляется
        :param closest_planet:
        :return:
        """
        if get_distance(self.get_coordinates()[0] + self.vx, self.get_coordinates()[1] + self.vy,
                        closest_planet.get_coordinates()[0],
                        closest_planet.get_coordinates()[1]) < closest_planet.radius:
            dist = get_distance(self.get_coordinates()[0], self.get_coordinates()[1],
                                closest_planet.get_coordinates()[0], closest_planet.get_coordinates()[1])
            cosx = (self.get_coordinates()[0] - closest_planet.get_coordinates()[0]) / dist
            siny = (self.get_coordinates()[1] - closest_planet.get_coordinates()[1]) / dist
            vector = math.sqrt(self.vx * self.vx + self.vy * self.vy)
            self.vx += vector * cosx
            self.vy += vector * siny
