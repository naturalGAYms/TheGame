from level import Level


class Game:
    def __init__(self):
        self.current_level: Level = None

    def run(self):
        while True:
            self.current_level.on_tick()


if __name__ == '__main__':
    game = Game()
