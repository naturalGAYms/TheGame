from game_objects.rocket import Rocket
from game_objects.hole import Hole


class Level:
    def __init__(self):
        self.rocket = Rocket()
        self.planets = []
        self.hole = Hole()
