from game_objects.game_object import GameObject
from program_variables import GLOBAL_WIDTH, GLOBAL_HEIGHT
import random
SCREEN_WIDTH = GLOBAL_WIDTH
SCREEN_HEIGHT = GLOBAL_HEIGHT

class Asteroid(GameObject):
    def __init__(self, x: int, y: int, id):
        super().__init__(x, y)
        self.vx = random.randint(1, 5)
        self.vy = random.randint(1, 5)
        self.shift_x = 0
        self.shift_y = 0
        self.delay = 10
        self.id = id

    def on_tick(self):
        if self.delay > 0:
            new_x = self.x + self.shift_x
            new_y = self.y + self.shift_y

            self.x = new_x % SCREEN_WIDTH
            self.y = new_y % SCREEN_HEIGHT
            self.delay -= 1
        else:
            self.shift_x = random.randint(-5, 5)
            self.shift_y = random.randint(-5, 5)
            self.delay = 10
