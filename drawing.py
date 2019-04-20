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
asteroid_pic = pygame.image.load('sprites/asteroid.png')


def draw_items(_level, surface: pygame.display):
    surface.blit(background_image, (0, 0))
    surface.blit(blackhole_image, _level.hole.get_coordinates())
    rocket_coords = _level.rocket.get_coordinates()
    rocket_angle = - _level.rocket.return_angle() * 57.32
    rocket_image_with_angle = rot_center(rocket_image, rocket_angle, rocket_coords)
    for planet in _level.planets:
        planet_pic = rocket_pics[0]
        planet_size_ratio = float(planet.radius) / float(planet_pic.get_rect().width)
        planet_rect = planet_pic.get_rect()
        scaled_size = get_scaled_size(planet_rect, planet_size_ratio)
        new_pic = pygame.transform.scale(planet_pic, scaled_size)
        planet_rect.move_ip(*planet.get_coordinates())
        surface.blit(new_pic, planet_rect)
    for asteroid in _level.asteroids:
        surface.blit(asteroid_pic, asteroid.get_coordinates())
    surface.blit(*rocket_image_with_angle)
    SingleColorBar(surface, 255, 0, 0, _level.rocket.fuel)
    pygame.display.flip()


def rot_center(image, angle, rocket_coords):
    rot_image = pygame.transform.rotate(image, angle)
    rect = image.get_rect()
    rect.move_ip(*rocket_coords)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect


def get_scaled_size(rect, ratio):
    return int(rect.height * ratio), int(rect.width * ratio)


def SingleColorBar(surface, color, x, y, value):
    xx=0
    for hp in range(value):
        pygame.draw.rect(surface, color, (x+xx, y, 1, 32), 0)
        xx += value/1001
