from level import Level
import pygame

GAME_NAME = 'Space ships'
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Game:
    def __init__(self):
        self.current_level: Level = None
        self.screen: pygame.display = None

    def init_game(self):
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)

    def run(self):
        while True:
            self.current_level.on_tick(self.screen, pygame.event.get())


if __name__ == '__main__':
    game = Game()
    game.init_game()
    pygame.display.set_caption(GAME_NAME)
    pygame.mouse.set_visible(False)
