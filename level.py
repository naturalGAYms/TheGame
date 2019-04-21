import pygame
import time

from game_objects.rocket import Rocket
from game_objects.hole import Hole
from game_objects.planet import Planet
from game_objects.human import Human
from process_events import process_key_event
from drawing import draw_items
from process_logic import run_logic
from game_objects.asteroid import Asteroid


class Level:
    def __init__(self, start_coords: (int, int), finish_coords: (int, int), planets, asteraids):
        self.rocket = Rocket(*start_coords)
        self.planets = planets
        self.hole = Hole(*finish_coords)
        self.asteroids = asteraids
        self.is_game_over = False
        self.is_completed = False
        self.rotating_left = False
        self.rotating_right = False
        self.boost_active = False
        self.score = len(planets)
        self.is_last = False

    def on_tick(self, surface: pygame.display, events, game):
        process_key_event(self, events, game)
        run_logic(self)
        draw_items(self, surface)
        if not self.rocket.alive:
            expl = pygame.image.load('sprites/explosion.png')
            surface.blit(pygame.transform.scale(expl, (70, 70)), (self.rocket.x - 35, self.rocket.y - 35))
            pygame.display.flip()



