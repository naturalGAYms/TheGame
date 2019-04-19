import pygame


def process_key_event(level, events):
    for event in filter(lambda x: x.type == pygame.KEYDOWN or x.type == pygame.QUIT, events):
        if event.type == pygame.QUIT:
            level.is_game_over = True
            return
        if event.key == pygame.K_SPACE:
            level.rocket.change_boost()
        if event.key == pygame.K_a:
            level.rocket.change_angle()
        if event.key == pygame.K_d:
            level.rocket.change_angle()
