import pygame

# from level import Level

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def draw_items(level, screen: pygame.display):
    screen.fill(GREEN)
    pygame.display.flip()
