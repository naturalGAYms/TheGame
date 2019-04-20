import pygame
from random import randint

import level

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

background_image = pygame.image.load('sprites/background0.jpg')
rocket_image = pygame.image.load('sprites/spaceship0.png')
rocket_pics = [pygame.image.load('sprites/p1.png'),
               pygame.image.load('sprites/p2.png'),
               pygame.image.load('sprites/p3.png'),
               pygame.image.load('sprites/p4.png'),
               pygame.image.load('sprites/p5.png'),
               pygame.image.load('sprites/p6.png'),
               pygame.image.load('sprites/p7.png'),
               pygame.image.load('sprites/p8.png'),
               pygame.image.load('sprites/p9.png'),
               pygame.image.load('sprites/p10.png')
               ]
blackhole_image = pygame.image.load('sprites/blackhole.png')

def draw_items(_level, surface: pygame.display):
    surface.blit(background_image, (0, 0))
    surface.blit(blackhole_image, _level.hole.get_coordinates())
    rocket_coords = _level.rocket.get_coordinates()
    rocket_angle = - _level.rocket.return_angle() * 57.32
    rocket_image_with_angle = rot_center(rocket_image, rocket_angle, rocket_coords)
    surface.blit(*rocket_image_with_angle)
    for planet in _level.planets:
        planet_pic = rocket_pics[0]
        planet_size_ratio = float(planet.radius) / float(planet_pic.get_rect().width)
        planet_rect = planet_pic.get_rect()
        surface.blit(planet_pic,
                     scale_and_place(planet_rect, planet_size_ratio, planet.get_coordinates()))
    pygame.display.flip()


def rot_center(image, angle, rocket_coords):
    rot_image = pygame.transform.rotate(image, angle)
    rect = image.get_rect()
    rect.move_ip(*rocket_coords)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect


def scale_and_place(rect, ratio, coords):
    return pygame.Rect(*coords, rect.height * ratio, rect.width * ratio)
