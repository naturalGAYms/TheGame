class GameObject:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coordinates(self) -> (int, int):
        return self.x, self.y
