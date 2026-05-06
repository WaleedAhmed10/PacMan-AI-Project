from constraints import DOT, EMPTY, POWER_PELLET, TILE_SIZE, WALL, WHITE, YELLOW
from maze_layout import FRUIT_TILE


class maze:
    def __init__layout (self, layout):
        self.layout = layout
        self.grid = deep_copy(layout)
        self.original_grid = deep_copy(layout)
        self.total_dots = count_all(DOT, POWER_PELLET, layout)
        self.dots_eaten = 0
        self.power_pellets_eaten = 0
        self.fruit_active = False
        self.fruit_timer  = 0
        self.fruit_type   = None
    def get_tile(x,y):
        if not is_valid_tile(x,y):
            return None
        return self.grid[y][x]
    def set_tile(x, y, value):
        self.grid[y][x] = value
    def remove_dot(x, y):  
        self.grid[y][x] = EMPTY
        self.dots_eaten += 1
    def remove_fruit():
        self.fruit_active = False
        self.grid[FRUIT_TILE.y][FRUIT_TILE.x] = EMPTY
    def update_fruit(delta_time, dots_eaten):
        if self.fruit_active:
            self.fruit_timer -= 1
            if self.fruit_timer <= 0:
                self.remove_fruit()
    def spawn_fruit():
        self.fruit_active = True
        self.fruit_timer = FRUIT_DURATION
        self.fruit_type = determine_fruit_type(self.dots_eaten)
        self.grid[FRUIT_TILE.y][FRUIT_TILE.x] = self.fruit_type
    def all_dots_eaten():
        return self.dots_eaten >= self.total_dots
    def all_dots_eaten():
        return self.dots_eaten >= self.total_dots
    def remaining_dots():
        return self.total_dots - self.dots_eaten
    def is_wall(x, y):
        return self.grid[y][x] == WALL
    def draw(screen):
        for row in range(ROWS):
            for col in range(COLS):
                tile = self.grid[row][col]
                x, y = col * TILE_SIZE, row * TILE_SIZE
            if tile == WALL:
                draw_rect(screen, DARK_BLUE, x, y, TILE_SIZE, TILE_SIZE)
                draw_wall_borders(screen, col, row)
            elif tile == DOT:
                draw_circle(screen, YELLOW, x + TILE_SIZE // 2, y + TILE_SIZE // 2, 4)
            elif tile == POWER_PELLET:
                if (current_time // 300) % 2 == 0:
                    draw_circle(screen, WHITE, center=(x + TILE_SIZE/2, y + TILE_SIZE/2), radius=6)
            elif tile in FRUIT_TYPES:
                draw_fruit_sprite(screen, self.fruit_type, x, y)
            def reset():
                self.grid = deep_copy(self.original_grid)
                self.dots_eaten = 0
                self.fruit_active = False
                self.fruit_timer  = 0