import pygame
from program_variables import boost_power, G, angle_delta

IMPACT_RADIUS = 10


def run_logic(level):
    for planet in level.planets:
        if check_impact(*level.rocket.get_coordinates(),
                        *planet.get_coordinates()):
            level.rocket.take_human(planet.get_human())
            break
    level.rocket.move()
    if level.rotating_left:
        level.rocket.change_angle(-angle_delta)
    if level.rotating_right:
        level.rocket.change_angle(angle_delta)
    if check_impact(*level.rocket.get_coordinates(), *level.hole.get_coordinates()):
        level.is_finished = True


def check_impact(x1, y1, x2, y2):
    distance_square = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    radius_sum_square = 4 * IMPACT_RADIUS * IMPACT_RADIUS
    return distance_square <= radius_sum_square
