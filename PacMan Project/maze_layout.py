MAZE_GRID = [
    [ 2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2],  # row 0
    [ 2,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2],  # row 1
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2],  # row 2
    [ 2,  3,  2,  0,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  0,  2,  1,  2,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  3,  2],  # row 3
    [ 2,  1,  2,  0,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  0,  2,  1,  2,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  1,  2],  # row 4
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  1,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  1,  2],  # row 5
    [ 2,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2],  # row 6
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  1,  2,  2,  1,  2],  # row 7
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  1,  2,  0,  0,  0,  0,  0,  2,  2,  1,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  1,  2,  2,  1,  2],  # row 8
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  0,  0,  0,  0,  0,  0,  0,  2,  1,  2,  0,  4,  4,  4,  0,  2,  2,  1,  2,  2,  0,  0,  0,  0,  0,  0,  0,  2,  1,  2,  2,  1,  2],  # row 9
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  0,  2,  2,  2,  4,  2,  0,  2,  0,  0,  0,  4,  4,  4,  0,  0,  0,  2,  0,  2,  0,  2,  4,  2,  2,  2,  0,  2,  1,  2,  2,  1,  2],  # row 10
    [ 5,  0,  0,  0,  0,  0,  1,  2,  2,  0,  2,  0,  0,  4,  0,  0,  0,  0,  0,  0,  4,  4,  4,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  4,  2,  0,  2,  1,  0,  0,  0,  5],  # row 11  ← TUNNEL
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  0,  2,  0,  0,  4,  0,  0,  0,  0,  0,  0,  4,  4,  4,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  4,  2,  0,  2,  1,  2,  2,  1,  2],  # row 12
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  0,  2,  2,  2,  2,  2,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2,  0,  2,  0,  2,  2,  2,  2,  2,  0,  2,  1,  2,  2,  1,  2],  # row 13
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  0,  0,  0,  0,  0,  0,  0,  2,  1,  2,  0,  0,  0,  0,  0,  2,  2,  1,  2,  2,  0,  0,  0,  0,  0,  0,  0,  2,  1,  2,  2,  1,  2],  # row 14
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  1,  2,  2,  1,  2],  # row 15
    [ 2,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2],  # row 16
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2],  # row 17
    [ 2,  1,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  0,  2,  1,  2,  0,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  1,  2],  # row 18
    [ 2,  3,  2,  0,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  0,  2,  1,  2,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  0,  0,  0,  2,  1,  2,  3,  2],  # row 19
    [ 2,  1,  1,  2,  2,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  1,  1,  1,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,  2],  # row 20
    [ 2,  1,  1,  2,  2,  1,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  2,  1,  2,  0,  2,  1,  2,  0,  2,  1,  2,  2,  2,  2,  2,  1,  2,  2,  2,  2,  1,  1,  2,  1,  2],  # row 21
    [ 2,  1,  1,  2,  2,  1,  1,  2,  2,  0,  0,  0,  1,  0,  0,  0,  2,  2,  1,  2,  0,  2,  1,  2,  0,  2,  1,  2,  2,  0,  0,  0,  1,  0,  0,  0,  2,  1,  1,  2,  1,  2],  # row 22
    [ 2,  1,  1,  1,  1,  1,  1,  2,  2,  0,  2,  2,  2,  2,  2,  0,  2,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2,  2,  0,  2,  2,  2,  2,  2,  0,  2,  1,  1,  1,  1,  2],  # row 23
    [ 2,  2,  2,  2,  2,  2,  1,  2,  2,  0,  2,  2,  2,  2,  2,  0,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  0,  2,  2,  2,  2,  2,  0,  2,  2,  2,  2,  2,  2],  # row 24  ← Pac-Man start row
]

PACMAN_START   = (20, 23)

GHOST_HOUSE_CENTER = (20, 11)
GHOST_HOUSE_EXIT   = (20,  9)

BLINKY_START   = (20,  8)
PINKY_START    = (19, 11)
INKY_START     = (18, 11)
CLYDE_START    = (21, 11)

FRUIT_TILE     = (20, 13)

BLINKY_SCATTER = (41,  0)
PINKY_SCATTER  = ( 0,  0)
INKY_SCATTER   = (41, 24)
CLYDE_SCATTER  = ( 0, 24)

TUNNEL_ROW     = 11
TUNNEL_LEFT    = ( 0, 11)
TUNNEL_RIGHT   = (41, 11)

def get_tile(x, y):
    """Return tile value at grid position (x, y). Returns WALL if out of bounds."""
    if y < 0 or y >= len(MAZE_GRID):
        return 2   # WALL
    if x < 0 or x >= len(MAZE_GRID[0]):
        return 2   # WALL
    return MAZE_GRID[y][x]


def set_tile(x, y, value):
    """Set tile value at grid position (x, y)."""
    if 0 <= y < len(MAZE_GRID) and 0 <= x < len(MAZE_GRID[0]):
        MAZE_GRID[y][x] = value


def is_wall(x, y):
    """Return True if the tile at (x, y) is a wall."""
    return get_tile(x, y) == 2


def is_walkable(x, y):
    """Return True if Pac-Man or a ghost can walk on this tile."""
    tile = get_tile(x, y)
    return tile != 2   # everything except WALL is walkable


def count_dots():
    """Count total dots and power pellets remaining in the maze."""
    total = 0
    for row in MAZE_GRID:
        for tile in row:
            if tile == 1 or tile == 3:   # DOT or POWER_PELLET
                total += 1
    return total


def get_maze_dimensions():
    """Return (cols, rows) of the maze grid."""
    return len(MAZE_GRID[0]), len(MAZE_GRID)


def validate_maze():
    cols, rows = get_maze_dimensions()
    errors = []

    for r, row in enumerate(MAZE_GRID):
        if len(row) != cols:
            errors.append(f"Row {r} has {len(row)} cols, expected {cols}")

    if errors:
        for e in errors:
            print(f"[MAZE ERROR] {e}")
        raise ValueError("Maze layout is invalid. Fix errors above.")
    else:
        print(f"[MAZE OK] {cols} cols x {rows} rows — {count_dots()} dots total")


if __name__ == "__main__":
    validate_maze()