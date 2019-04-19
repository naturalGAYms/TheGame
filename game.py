from level import Level
import pygame

GAME_NAME = 'Space ships'
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Game:
    def __init__(self):
        self.current_level: Level = Level((0,0), (100,100))
        self.screen: pygame.display = None
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

    def init_game(self):
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        pygame.mouse.set_visible(False)

    def run(self):
        while True:
            self.current_level.on_tick(self.screen, pygame.event.get())
            self.clock.tick(60)
            if self.current_level.is_game_over:
                break


if __name__ == '__main__':
    game = Game()
    game.init_game()
    game.run()
