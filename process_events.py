import pygame


def process_key_event(level, events):
    for event in filter(lambda x: x.type == pygame.KEYDOWN, events):
        if event.type == pygame.QUIT:
            level.is_game_over = True
        if event.key == pygame.K_SPACE:
            level.rocket.change_boost()
        if event.key == pygame.K_a:
            level.rocket.change_angle()
        if event.key == pygame.K_d:
            level.rocket.change_angle()
