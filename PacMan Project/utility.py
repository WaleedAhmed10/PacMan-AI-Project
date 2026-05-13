<<<<<<< HEAD
from math import sqrt
from constants import TILE_SIZE, COLS, ROWS, UP, DOWN, LEFT, RIGHT

def tile_to_pixel(tile_x, tile_y):
    return (tile_x * TILE_SIZE + TILE_SIZE/2, tile_y * TILE_SIZE + TILE_SIZE/2)

def pixel_to_tile(pixel_x, pixel_y):
    return (pixel_x // TILE_SIZE, pixel_y // TILE_SIZE)

def wrap_tunnel(x, y):
    if x < 0:
        return (COLS - 1, y)
    elif x >= COLS:
        return (0, y)
    return (x, y)

def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean_distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def is_valid_tile(x, y):
    return 0 <= x < COLS and 0 <= y < ROWS
=======
def  tile_to_pixel(tile_x, tile_y):
    return (tile_x * TILE_SIZE + TILE_SIZE/2, tile_y * TILE_SIZE + TILE_SIZE/2)
def pixel_to_tile(pixel_x, pixel_y):
    return (pixel_x // TILE_SIZE, pixel_y // TILE_SIZE)
def wrap_tunnel(X, y):
    if X < 0: return (COLS - 1, y)
    elif X >= COLS: return (0, y)
    return (X, y)
def manhatten_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def euclidean_distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
def is_valid_tile(x, y):
    return 0 <= x < COLS and 0 <= y < ROWS
    if maze_is_wall(x, y):
        return False
    return True
def get_opp_direction(direction):
    if direction == UP: return DOWN
    if direction == DOWN: return UP
    if direction == LEFT: return RIGHT
    if direction == RIGHT: return LEFT
def bfs(start, target, maze):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    while queue:
        current = queue.popleft()
        if current == target:
            return path_from_parent(parent, target)
        for d in [UP, DOWN, LEFT, RIGHT]:
            next_tile = current + d
            next_tile = wrap_tunnel(next_tile)
            if next_tile not in visited and not maze.is_wall(next_tile.x, next_tile.y):
                visited.add(next_tile)
                parent[next_tile] = current
                queue.append(next_tile)
            return[]
        def path_from_parent(parent, target):
            path = []
            while target is not None:
                path.append(target)
                target = parent[target]
            return path[::-1]
>>>>>>> c9441631f6679ee1256bd6d0941b633cc3072f25
