class blinky(ghost):
    def __init__ (self, text):
        super().__init__(name="Blinky", color=RED, start_tile=ABOVE_HOUSE, scatter_target=TOP_RIGHT_CORNER, release_threshold=0)
    def get_target_tile(self, pacman, maze, all_ghosts):
        if self.state == CHASE:
            return pacman.tile
        elif self.state == SCATTER:
            return self.scatter_target
        elif self.state == FRIGHTENED_STATE:
            return self._get_frightened_target(pacman, maze, all_ghosts)
        elif self.state == EATEN:
            return self.house_tile
        elif remaining_dots < ELROY_THRESHOLD:
            self.speed = 2.2
            return (pacman.tile_x, pacman.tile_y)
class inky(ghost):
    def __init__ (self, text):
        super().__init__(name="Inky", color=CYAN, start_tile=CENTER_HOUSE, scatter_target=TOP_LEFT_CORNER, release_threshold=0)
    def get_target_tile(self, pacman, maze, all_ghosts):
        blinky = next(g for g in all_ghosts if g.name == "Blinky")
        if self.state == CHASE:
            target_x = pacman.tile_x + 2 * (pacman.tile_x - blinky.tile_x)
            target_y = pacman.tile_y + 2 * (pacman.tile_y - blinky.tile_y)
            return (target_x, target_y)
        elif self.state == SCATTER:
            return self.scatter_target
        elif self.state == FRIGHTENED_STATE:
            return self._get_frightened_target(pacman, maze, all_ghosts)
        elif self.state == EATEN:
            return self.house_tile

class pinky(ghost):
    def __init__ (self, text):
        super().__init__(name="Pinky", color=PINK, start_tile=LEFT_HOUSE, scatter_target=BOTTOM_RIGHT_CORNER, release_threshold=0)
    def get_target_tile(self, pacman, maze, all_ghosts):
        if self.state == CHASE:
            pivot_x = pacman.tile_x + pacman.direction.x * 2
            pivot_y = pacman.tile_y + pacman.direction.y * 2
            return (target_x, target_y)
            pinky  = all_ghosts["Blinky"]
            target_x = pivot_x + (pivot_x - blinky.tile_x)
            target_y = pivot_y + (pivot_y - blinky.tile_y)
            return (target_x, target_y)
        elif self.state == SCATTER:
            return self.scatter_target
        elif self.state == FRIGHTENED_STATE:
            return self._get_frightened_target(pacman, maze, all_ghosts)
        elif self.state == EATEN:
            return self.house_tile
class clyde(ghost):
    def __init__ (self, text):
        super().__init__(name="Clyde", color = ORANGE, start_tile=RIGHT_HOUSE, scatter_target=BOTTOM_LEFT_CORNER, release_threshold=0)
    def get_target_tile(self, pacman, maze, all_ghosts):
        if self.state == CHASE:
            dist = euclidean_distance( (self.tile_x, self.tile_y), (pacman.tile_x, pacman.tile_y))
            if dist > 8:
                return pacman.tile
            else:
                return self.scatter_target