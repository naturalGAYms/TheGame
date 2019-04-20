import pygame
import math
from program_variables import boost_power, G, angle_delta

IMPACT_RADIUS = 50


def check_level_completion(level):
    rocket_cords = level.rocket.get_coordinates()
    hole_cords = level.hole.get_coordinates()
    delta = abs(rocket_cords[0] - hole_cords[0] - level.hole.shift_to_center) + abs(
        rocket_cords[1] - hole_cords[1] - level.hole.shift_to_center)
    if delta < 80 and level.score == 0:
        return True
    return False


def run_logic(level):
    level.rocket.move()
    for asteroid in level.asteroids:
        asteroid.on_tick()
    if level.rotating_left:
        level.rocket.change_angle(-angle_delta)
    if level.rotating_right:
        level.rocket.change_angle(angle_delta)
    if level.boost_active:
        level.rocket.enable_boost()
    for planet in level.planets:
        if planet.human and check_impact(*level.rocket.get_coordinates(), *planet.human.get_coordinates()):
            planet.get_human()
            sound1 = pygame.mixer.Sound('sprites/hum.wav')
            sound1.play()
            level.score -= 1
        level.rocket.vx += planet.get_gravity(level.rocket)[0] / 100
        level.rocket.vy += planet.get_gravity(level.rocket)[1] / 100
        level.rocket.collision_with_planet(planet)

    if check_level_completion(level):
        sound1 = pygame.mixer.Sound('sprites/hole.wav')
        sound1.play()
        level.is_completed = True

def check_impact(x1, y1, x2, y2):
    distance_square = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    radius_sum_square = 4 * IMPACT_RADIUS * IMPACT_RADIUS
    return distance_square <= radius_sum_square


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
