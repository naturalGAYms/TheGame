import pygame

import level

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def draw_items(_level, screen: pygame.display):
    screen.fill(GREEN)
    # level.Level.rocket
    pygame.display.flip()
