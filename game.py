from level import Level
import pygame
from game_objects.planet import Planet
from game_objects.human import Human
from game_objects.asteroid import Asteroid
from program_variables import GLOBAL_WIDTH, GLOBAL_HEIGHT
import time
import copy

GAME_NAME = 'Space ships'
SCREEN_WIDTH = GLOBAL_WIDTH
SCREEN_HEIGHT = GLOBAL_HEIGHT


class Game:
    def __init__(self):
        self.levels = [
            Level((30, 30), (300, 400),
                  [
                      Planet(200, 200, 60, Human(2, 200, 200, 60)),
                      Planet(1000, 304, 50, Human(0.8, 1000, 304, 50)),
                      Planet(500, 601, 35, Human(1.3, 500, 601, 35)),
                  ],
                  [
                      Asteroid(800, 400, 1),
                      Asteroid(200, 100, 2),
                      Asteroid(700, 350, 3),
                      Asteroid(110, 773, 1)
                  ]),
            Level((400, 40), (600, 450),
                  [
                      Planet(736, 309, 100, Human(1, 736, 309, 100)),
                      Planet(516, 608, 70, Human(2.3, 516, 608, 70)),
                      Planet(100, 100, 65, Human(3.2, 100, 100, 65)),
                  ],
                  [
                      Asteroid(800, 400, 1),
                      Asteroid(200, 100, 2),
                      Asteroid(213, 123, 3),
                      Asteroid(132, 321, 1)
                  ]),
            Level((100, 400), (650, 400),
                  [
                      Planet(407, 400, 35, Human(0.1, 407, 400, 35)),
                      Planet(500, 177, 25, Human(3, 500, 177, 25)),
                      Planet(100, 302, 17, Human(2.4, 100, 302, 17))],
                  [
                      Asteroid(800, 400, 1),
                      Asteroid(200, 100, 2),
                      Asteroid(213, 123, 3),
                      Asteroid(132, 321, 1)
                  ]),
            Level((800, 40), (400, 200),
                  [
                      Planet(100, 100, 65, Human(3.2, 100, 100, 65)),
                      Planet(1000, 305, 100, Human(2.6, 1000, 305, 100)),
                      Planet(503, 600, 70, Human(3, 503, 600, 70)),
                  ],
                  [
                      Asteroid(800, 400, 1),
                      Asteroid(200, 100, 2),
                      Asteroid(213, 123, 3),
                      Asteroid(132, 321, 1)
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
            self.current_level = copy.deepcopy(self.levels[self.index])
        except:
            _img = pygame.image.load(f'sprites/en.jpg')
            self.surface.blit(pygame.transform.scale(_img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
            pygame.display.flip()
            time.sleep(6)
        self.index += 1

    def restart_level(self):
        self.index -= 1
        self.current_level = copy.deepcopy(self.levels[self.index])
        self.index += 1

    def init_game(self):
        pygame.init()
        file = 'sprites/aud.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.display.set_caption(GAME_NAME)
        pygame.mouse.set_visible(False)

    def run(self):
        self.get_next_level()
        img = None
        counter = 0
        while True:
            self.clock.tick(60)
            if self.delay > 0:
                self.surface.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
                self.delay -= 1
                pygame.display.flip()
                continue
            self.current_level.on_tick(self.surface, pygame.event.get(), self)
            if self.current_level.is_completed:
                img = pygame.image.load(f'sprites/s/{self.index}.png')
                self.delay = 7 * 60
                print(self.delay)
                self.get_next_level()
            if self.current_level.is_game_over or self.index > 4:
                break
            if not self.current_level.rocket.alive:
                counter += 1
                print(counter)
            if counter > 60:
                counter = 0
                self.restart_level()


def main():
    game = Game()
    game.init_game()
    game.run()


if __name__ == '__main__':
    main()
