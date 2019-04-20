import pygame
import sys
from program_variables import boost_power, G, angle_delta


def process_key_event(level, events):
    for event in filter(lambda x: x.type == pygame.KEYDOWN or pygame.QUIT or pygame.KEYUP, events):
        if event.type == pygame.QUIT:
            level.is_game_over = True
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_SPACE:
                level.boost_active = True
            if event.key == pygame.K_w:
                level.boost_active = True
            if event.key == pygame.K_UP:
                level.boost_active = True
            if event.key == pygame.K_a:
                level.rotating_left = True
            if event.key == pygame.K_LEFT:
                level.rotating_left = True
            if event.key == pygame.K_d:
                level.rotating_right = True
            if event.key == pygame.K_RIGHT:
                level.rotating_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                level.boost_active = False
            if event.key == pygame.K_w:
                level.boost_active = False
            if event.key == pygame.K_UP:
                level.boost_active = False
            if event.key == pygame.K_a:
                level.rotating_left = False
            if event.key == pygame.K_LEFT:
                level.rotating_left = False
            if event.key == pygame.K_d:
                level.rotating_right = False
            if event.key == pygame.K_RIGHT:
                level.rotating_right = False
