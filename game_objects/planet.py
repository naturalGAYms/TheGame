from game_objects.game_object import GameObject
from game_objects.human import Human
from game_objects.rocket import Rocket
from program_variables import G, mass_of_rocket
import math


class Planet(GameObject):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius = radius
        self.gravity = G * (math.pi * self.radius * self.radius)

    def get_gravity(self, rocket: Rocket) -> float:
        return (self.gravity * mass_of_rocket) / pow(self.get_distance_to_rocket(rocket), 2)

    def get_human(self) -> Human:
        pass

    def get_human_angle_coordinate(self) -> float:
        pass

    def get_distance_to_rocket(self, rocket: Rocket) -> float:
        planet = self.get_coordinates()
        rocket = rocket.get_coordinates()
        return math.sqrt((planet[0] - rocket[0]) * (planet[0] - rocket[0]) +
                         (planet[1] - rocket[1]) * (planet[1] - rocket[1]))
