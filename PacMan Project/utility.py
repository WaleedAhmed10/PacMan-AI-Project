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
