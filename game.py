from level import Level
import pygame

GAME_NAME = 'Space ships'
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800


class Game:
    def __init__(self):
        self.levels = [
            Level((0, 0), (300, 400)),
            Level((400, 40), (600, 600)),
            Level((100, 400), (1000, 400)),
            Level((800, 40), (400, 100)),
            Level((10, 40), (1000, 300)),
        ]
        self.index = 0
        self.current_level: Level = Level((0, 0), (100, 100))
        self.screen: pygame.display = None
        # size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

    def get_next_level(self):
        self.current_level = self.levels[self.index]
        self.index += 1

    def init_game(self):
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        pygame.mouse.set_visible(False)

    def run(self):
        self.get_next_level()
        while True:
            self.current_level.on_tick(self.surface, pygame.event.get())
            self.clock.tick(60)
            if self.current_level.is_completed:
                self.get_next_level()
            if self.current_level.is_game_over or self.index > 4:
                break


if __name__ == '__main__':
    game = Game()
    game.init_game()
    game.run()
