import pygame

IMPACT_RADIUS = 10


def run_logic(level):
    for planet in level.planets:
        if check_impact(*level.rocket.get_coordinates(),
                        *planet.get_coordinates()):
            level.rocket.take_human(planet.get_human())
            break
    if check_impact(level.rocket, level.hole):
        level.is_finished = True


def check_impact(x1, y1, x2, y2):
    distance_square = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    radius_sum_square = 4 * IMPACT_RADIUS * IMPACT_RADIUS
    return distance_square <= radius_sum_square

