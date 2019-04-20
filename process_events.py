import pygame
from program_variables import boost_power, G, angle_delta


def process_key_event(level, events):
    for event in filter(lambda x: x.type == pygame.KEYDOWN or x.type == pygame.QUIT, events):
        if event.type == pygame.QUIT:
            level.is_game_over = True
            return
        if event.key == pygame.K_SPACE:
            level.rocket.enable_boost()
        if event.key == pygame.K_a:
            level.rocket.change_angle(-angle_delta)
        if event.key == pygame.K_d:
            level.rocket.change_angle(angle_delta)
