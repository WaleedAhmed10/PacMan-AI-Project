from copy import deepcopy
from constraints import DOT, EMPTY, POWER_PELLET

class Maze:
    def __init__(self, layout):
        self.layout = layout
        self.grid = deepcopy(layout)

    def get_tile(self, x, y):
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]):
            return self.grid[y][x]
        return None

    def set_tile(self, x, y, value):
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]):
            self.grid[y][x] = value
