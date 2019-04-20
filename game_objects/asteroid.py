from game_objects.game_object import GameObject
import random


class Asteroid(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.vx = random.randint(1, 5)
        self.vy = random.randint(1, 5)
        self.shift_x = 0
        self.shift_y = 0
        self.delay = 10

    def on_tick(self):
        if self.delay > 0:
            self.x += self.shift_x
            self.y += self.shift_y
            self.delay -= 1
        else:
            self.shift_x = random.randint(-5, 5)
            self.shift_y = random.randint(-5, 5)
            self.delay = 10
