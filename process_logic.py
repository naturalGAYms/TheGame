import pygame
import math
from program_variables import boost_power, G, angle_delta

IMPACT_RADIUS = 0


def check_level_completion(level):
    rocket_cords = level.rocket.get_coordinates()
    hole_cords = level.hole.get_coordinates()
    delta = abs(rocket_cords[0] - hole_cords[0] - level.hole.shift_to_center) + abs(
        rocket_cords[1] - hole_cords[1] - level.hole.shift_to_center)
    if delta < 80:
        return True
    return False


def run_logic(level):
    for planet in level.planets:
        if check_impact(*level.rocket.get_coordinates(),
                        *planet.get_coordinates()):
            # level.rocket.take_human(planet.get_human())
            break
        level.rocket.vx += planet.get_gravity(level.rocket)[0] / 100
        level.rocket.vy += planet.get_gravity(level.rocket)[1] / 100
    level.rocket.move()
    if level.rotating_left:
        level.rocket.change_angle(-angle_delta)
    if level.rotating_right:
        level.rocket.change_angle(angle_delta)
    if level.boost_active:
        level.rocket.enable_boost()

    if check_level_completion(level):
        level.is_completed = True


def check_impact(x1, y1, x2, y2):
    distance_square = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    radius_sum_square = 4 * IMPACT_RADIUS * IMPACT_RADIUS
    return distance_square <= radius_sum_square
