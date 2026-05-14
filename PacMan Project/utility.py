from math import sqrt
from heapq import heappush, heappop
from constants import TILE_SIZE, COLS, ROWS, UP, DOWN, LEFT, RIGHT

def tile_to_pixel(tile_x, tile_y):
    return (tile_x * TILE_SIZE + TILE_SIZE // 2, tile_y * TILE_SIZE + TILE_SIZE // 2)

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
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_valid_tile(x, y):
    return 0 <= x < COLS and 0 <= y < ROWS

def get_opp_direction(direction):
    if direction == UP:    return DOWN
    if direction == DOWN:  return UP
    if direction == LEFT:  return RIGHT
    if direction == RIGHT: return LEFT

def path_from_parent(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return path[::-1]

def astar(start, target, maze):
    open_set = [(0, start)]
    parent   = {start: None}
    g_score  = {start: 0}
    while open_set:
        _, current = heappop(open_set)
        if current == target:
            return path_from_parent(parent, target)
        for d in [UP, DOWN, LEFT, RIGHT]:
            nx, ny   = wrap_tunnel(current[0] + d[0], current[1] + d[1])
            neighbor = (nx, ny)
            if maze.is_wall(nx, ny):
                continue
            new_g = g_score[current] + 1
            if neighbor not in g_score or new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                f = new_g + manhattan_dist(neighbor, target)
                heappush(open_set, (f, neighbor))
                parent[neighbor] = current
    return []