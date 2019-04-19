import pygame

from game_objects.rocket import Rocket
from game_objects.hole import Hole
from process_events import process_key_event


class Level:
    def __init__(self, start_coords: (int, int), finish_coords: (int, int)):
        self.rocket = Rocket(*start_coords)
        self.planets = []
        self.hole = Hole(*finish_coords)
        self.is_finished: bool = False

    def on_tick(self, screen: pygame.display, events):
        process_key_event(self, events)
        # ToDo вызов изменений логики
        # ToDo вызов отрисовки
        pass
