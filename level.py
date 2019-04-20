import pygame

from game_objects.rocket import Rocket
from game_objects.hole import Hole
from process_events import process_key_event
from drawing import draw_items
from process_logic import run_logic


class Level:
    def __init__(self, start_coords: (int, int), finish_coords: (int, int)):
        self.rocket = Rocket(*start_coords)
        self.planets = []
        self.hole = Hole(*finish_coords)
        self.is_game_over = False

    def on_tick(self, surface: pygame.display, events):
        process_key_event(self, events)
        run_logic(self)
        draw_items(self, surface)
