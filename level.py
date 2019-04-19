from game_objects.rocket import Rocket
from game_objects.hole import Hole


class Level:
    def __init__(self, start_coords: (int, int), finish_coords: (int, int)):
        self.rocket = Rocket(*start_coords)
        self.planets = []
        self.hole = Hole(*finish_coords)

    def on_tick(self):
        # ToDo вызов событий
        # ToDo вызов изменений логики
        # ToDo вызов отрисовки
        pass
