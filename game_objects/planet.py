from game_objects.game_object import GameObject
from game_objects.human import Human
from program_variables import G, mass_of_rocket
import math


class Planet(GameObject):
    def __init__(self, x: int, y: int, radius: int, human: Human):
        super().__init__(x, y)
        self.radius = radius
        self.human = human
        self.gravity = G * (math.pi * self.radius * self.radius)

    def get_gravity(self, rocket) -> float:
        return (self.gravity * mass_of_rocket) / pow(self.get_distance_to_rocket(rocket), 2)

    def get_human(self) -> Human:
        return self.human

    def get_human_angle_coordinate(self) -> float:
        human = self.human.get_coordinates()
        center = self.get_coordinates()
        dx = human[0] - center[0]
        dy = human[1] - center[1]
        return math.atan(dy / float(dx))

    def get_distance_to_rocket(self, rocket) -> float:
        planet = self.get_coordinates()
        rocket = rocket.get_coordinates()
        return math.sqrt((planet[0] - rocket[0]) * (planet[0] - rocket[0]) +
                         (planet[1] - rocket[1]) * (planet[1] - rocket[1]))

    def pickup_human(self, rocket):
        human = self.human.get_coordinates()
        rocket = rocket.get_coordinates()
        distance = math.sqrt((human[0] - rocket[0]) * (human[0] - rocket[0]) +
                         (human[1] - rocket[1]) * (human[1] - rocket[1]))
        if distance < 5:
            self.human = False
