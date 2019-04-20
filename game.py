from level import Level
import pygame
from game_objects.planet import Planet
from game_objects.human import Human

GAME_NAME = 'Space ships'
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800


class Game:
    def __init__(self):
        self.levels = [
            Level((50, 50), (300, 400), [
                Planet(100, 100, 120, Human(100, 100)),
                Planet(1000, 300, 100, Human(100, 100)),
                Planet(500, 600, 70, Human(100, 100)),]
                  ),
            Level((400, 40), (600, 600), []),
            Level((100, 400), (1000, 400), []),
            Level((800, 40), (400, 100), []),
            Level((10, 40), (1000, 300), []),
        ]
        self.index = 0
        self.current_level: Level = Level((0, 0), (100, 100), [])
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
            # rocket_cords = self.current_level.rocket.get_coordinates()
            # if rocket_cords[0] < 0 or rocket_cords[1] > SCREEN_WIDTH or rocket_cords[1] < 0 or rocket_cords[
            #     1] > SCREEN_HEIGHT:
            #     break
            if self.current_level.is_game_over or self.index > 4:
                break


if __name__ == '__main__':
    game = Game()
    game.init_game()
    game.run()
