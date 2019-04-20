import pygame
from random import randint

import level
import random

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
human_pic = pygame.image.load('sprites/chelik.png')


def draw_items(_level, surface: pygame.display):
    surface.blit(background_image, (0, 0))
    surface.blit(blackhole_image, _level.hole.get_coordinates())
    SingleColorBar(surface, RED, 0, 0, _level.rocket.fuel)
    rocket_coords = _level.rocket.get_coordinates()
    rocket_angle = - _level.rocket.return_angle() * 57.32
    rocket_image_with_angle = rot_center(rocket_image, rocket_angle, rocket_coords)

    for planet in _level.planets:
        planet_pic = rocket_pics[(planet.x + planet.y) % 10]
        new_pic = pygame.transform.scale(planet_pic, (planet.radius * 2, planet.radius * 2))
        surface.blit(new_pic, (planet.x - planet.radius, planet.y - planet.radius))
        human_coords = planet.human.get_coordinates()
        human_image = human_pic.transform.scale(surface, 15, 15)
        human_image_with_angle = rot_center(human_image, planet.human.angle, human_coords)
        surface.blit(*human_image_with_angle)
        # pygame.draw.circle(surface, 255, planet.get_coordinates(), planet.radius, 12)

        # draw_at_center(surface, new_pic, planet_rect)
    for asteroid in _level.asteroids:
        asteroid_rect = pygame.Rect(0, 0, *asteroid.get_coordinates())
        draw_asteroid_at_center(surface, asteroid_pic, asteroid_rect)

    surface.blit(*rocket_image_with_angle)
    pygame.display.flip()


def rot_center(image, angle, rocket_coords):
    rot_image = pygame.transform.rotate(image, angle)
    rect = image.get_rect()
    rect.move_ip(*rocket_coords)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, (rot_rect[0] - 35, rot_rect[1] - 7.5)


def get_scaled_size(rect, ratio):
    return int(rect.height * ratio), int(rect.width * ratio)


def SingleColorBar(surface, color, x, y, value):
    xx = 0
    for hp in range(value):
        pygame.draw.rect(surface, color, (x + xx, y, 1, 32), 0)
        xx += value / 10000


# def draw_at_center(surface, picture, rect):
#     surface.blit(picture, (rect.left - picture.get_width() // 2, rect.top - picture.get_height() // 2))


def draw_asteroid_at_center(surface, picture, rect):
    surface.blit(picture, (rect.width - picture.get_width() // 2, rect.height - picture.get_height() // 2))
