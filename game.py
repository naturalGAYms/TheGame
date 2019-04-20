from level import Level
import pygame
import sys
from game_objects.planet import Planet
from game_objects.human import Human
from game_objects.asteroid import Asteroid
import time

GAME_NAME = 'Space ships'
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 650


class Game:
    def __init__(self):
        self.levels = [
            Level((30, 30), (300, 400),
                  [
                      Planet(200, 200, 60, Human(100, 100)),
                      Planet(1000, 304, 50, Human(100, 100)),
                      Planet(500, 601, 35, Human(100, 100)),
                      Planet(407, 400, 35, Human(100, 100)),
                      Planet(500, 177, 25, Human(100, 100)),
                      Planet(100, 302, 17, Human(100, 100))],
                  [
                      Asteroid(800, 400),
                      Asteroid(200, 100),
                      Asteroid(700, 350),
                      Asteroid(110, 773)
                  ]),
            Level((400, 40), (600, 450),
                  [
                      Planet(347, 136, 80, Human(100, 100)),
                      Planet(736, 309, 100, Human(100, 100)),
                      Planet(516, 608, 70, Human(100, 100)),
                      Planet(100, 100, 65, Human(100, 100)),
                      Planet(994, 490, 100, Human(100, 100)),
                      Planet(184, 443, 100, Human(100, 100)),
                      Planet(516, 608, 70, Human(100, 100))
                  ],
                  [
                      Asteroid(800, 400),
                      Asteroid(200, 100),
                      Asteroid(213, 123),
                      Asteroid(132, 321)
                  ]),
            Level((100, 400), (650, 400),
                  [
                      Planet(428, 951, 59, Human(100, 100)),
                      Planet(99, 110, 37, Human(100, 100)),
                      Planet(506, 601, 70, Human(100, 100)),
                      Planet(600, 101, 87, Human(100, 100)),
                      Planet(736, 309, 100, Human(100, 100))],
                  [
                      Asteroid(800, 400),
                      Asteroid(200, 100),
                      Asteroid(213, 123),
                      Asteroid(132, 321)
                  ]),
            Level((800, 40), (400, 200),
                  [
                      Planet(100, 359, 120, Human(100, 100)),
                      Planet(1000, 305, 100, Human(100, 100)),
                      Planet(503, 600, 70, Human(100, 100)),
                      Planet(570, 312, 22, Human(100, 100)),
                      Planet(503, 861, 35, Human(100, 100)),
                  ],
                  [
                      Asteroid(800, 400),
                      Asteroid(200, 100),
                      Asteroid(213, 123),
                      Asteroid(132, 321)
                  ]),
        ]
        self.index = 0
        self.current_level: Level = Level((0, 0), (100, 100), [], [])
        self.screen: pygame.display = None
        # size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        # self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.delay = 0

    def get_next_level(self):
        try:
            self.current_level = self.levels[self.index]
        except:
            _img = pygame.image.load(f'sprites/en.jpg')
            self.surface.blit(pygame.transform.scale(_img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
            pygame.display.flip()
            time.sleep(6)
        self.index += 1

    def init_game(self):
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        pygame.mouse.set_visible(False)

    def run(self):
        self.get_next_level()
        img = None
        while True:
            self.clock.tick(60)
            if self.delay > 0:
                self.surface.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
                self.delay -= 1
                pygame.display.flip()
                continue
            self.current_level.on_tick(self.surface, pygame.event.get())
            if self.current_level.is_completed:
                img = pygame.image.load(f'sprites/s/{self.index}.png')
                self.delay = 7 * 60
                print(self.delay)
                self.get_next_level()
            if self.current_level.is_game_over or self.index > 4:
                break


def main():
    game = Game()
    game.init_game()
    game.run()


if __name__ == '__main__':
    main()
