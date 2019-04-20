import pygame

import level

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

background_image = pygame.image.load('sprites/background.jpg')
rocket_image = pygame.image.load('sprites/spaceship0.png')


def draw_items(_level, surface: pygame.display):
    surface.blit(background_image, (0, 0))
    rocket_coords = _level.rocket.get_coordinates()
    rocket_angle = - _level.rocket.return_angle() * 57.32
    rocket_image_with_angle = pygame.transform.rotate(rocket_image, rocket_angle)
    surface.blit(rocket_image_with_angle, rocket_coords)
    pygame.display.flip()
