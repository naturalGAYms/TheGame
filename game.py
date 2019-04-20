from level import Level
import pygame
from game_objects.planet import Planet
from game_objects.human import Human
from game_objects.asteroid import Asteroid

GAME_NAME = 'Space ships'
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 650


class Game:
    def __init__(self):
        self.levels = [
            Level((30, 30), (300, 400),
                  [
                      Planet(200, 200, 60, Human(100, 100)),
                      Planet(1000, 300, 50, Human(100, 100)),
                      Planet(500, 600, 35, Human(100, 100)), ],
                  [
                      Asteroid(800, 400),
                      Asteroid(200, 100)
                  ]),
            Level((400, 40), (600, 600),
                  [
                      Planet(100, 100, 120, Human(100, 100)),
                      Planet(1000, 300, 100, Human(100, 100)),
                      Planet(500, 600, 70, Human(100, 100)), ],
                  [
                      Asteroid(800, 400),
                      Asteroid(200, 100)
                  ]),
            Level((100, 400), (1000, 400),
                  [
                      Planet(100, 100, 120, Human(100, 100)),
                      Planet(1000, 300, 100, Human(100, 100)),
                      Planet(500, 600, 70, Human(100, 100)), ],
                  [
                      Asteroid(800, 400),
                      Asteroid(200, 100)
                  ]),
            Level((800, 40), (400, 100),
                  [
                      Planet(100, 100, 120, Human(100, 100)),
                      Planet(1000, 300, 100, Human(100, 100)),
                      Planet(500, 600, 70, Human(100, 100)), ],
                  [
                      Asteroid(800, 400),
                      Asteroid(200, 100)
                  ]),
            Level((10, 40), (1000, 300),
                  [
                      Planet(100, 100, 120, Human(100, 100)),
                      Planet(1000, 300, 100, Human(100, 100)),
                      Planet(500, 600, 70, Human(100, 100)), ],
                  [
                      Asteroid(800, 400),
                      Asteroid(200, 100)
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
        self.current_level = self.levels[self.index]
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
