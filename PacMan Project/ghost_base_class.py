from constraints import CHASE, TILE_SIZE
import pygame
import math
import random
from constants import *

def tile_to_pixel(tx, ty):
    return (tx * TILE_SIZE + TILE_SIZE // 2, ty * TILE_SIZE + TILE_SIZE // 2)

def pixel_to_tile(px, py):
    return px // TILE_SIZE, py // TILE_SIZE

def euclid_dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def opposite(d):
    return (-d[0], -d[1])

def wrap(tx, ty, cols):
    if tx < 0: tx = cols - 1
    elif tx >= cols: tx = 0
    return tx, ty


class Ghost:

    RELEASE_THRESHOLD = 0
    SPD_NORMAL    = 1.8
    SPD_FRIGHTENED = 1.0
    SPD_EATEN     = 3.5

    def __init__(self, name, color, start_tile, scatter_target,
                 house_tile, exit_tile, cols):
        self.name           = name
        self.color          = color
        self.start_tile     = start_tile
        self.scatter_target = scatter_target
        self.house_tile     = house_tile
        self.exit_tile      = exit_tile
        self.cols           = cols

        self.tile_x, self.tile_y = start_tile
        px, py = tile_to_pixel(*start_tile)
        self.pixel_x, self.pixel_y = float(px), float(py)

        self.direction  = UP
        self.speed      = self.SPD_NORMAL * TILE_SIZE / 60.0
        self.state      = HOUSE
        self.prev_state = CHASE

        self.dot_counter         = 0
        self.frightened_timer    = 0
        self.is_flashing         = False
        self.flash_toggle        = False
        self.flash_timer         = 0
        self.score_display_timer = 0
        self.eaten_score         = 0
        self.bounce_offset       = 0.0
        self.bounce_dir          = 1
        self.anim_frame          = 0
        self.anim_timer          = 0

    @property
    def center(self):
        return (int(self.pixel_x), int(self.pixel_y))

    @property
    def tile(self):
        return (self.tile_x, self.tile_y)

    def update(self, dt, pacman, maze, all_ghosts):
        if self.score_display_timer > 0:
            self.score_display_timer -= dt
            return

        if self.state == HOUSE:
            self._house(dt)
        elif self.state == FRIGHTENED_STATE:
            self._frightened_tick(dt)
            self._move(maze, pacman, all_ghosts)
        elif self.state == EATEN:
            self._move(maze, pacman, all_ghosts)
            self._check_house()
        else:
            self._move(maze, pacman, all_ghosts)

        self.anim_timer += dt
        if self.anim_timer >= 200:
            self.anim_timer = 0
            self.anim_frame ^= 1

    def _house(self, dt):
        self.bounce_offset += self.bounce_dir * self.bounce_speed if hasattr(self, 'bounce_speed') else self.bounce_dir * 0.5
        if abs(self.bounce_offset) >= 6:
            self.bounce_dir *= -1
        if self.dot_counter >= self.RELEASE_THRESHOLD:
            self.tile_x, self.tile_y = self.exit_tile
            px, py = tile_to_pixel(self.tile_x, self.tile_y)
            self.pixel_x, self.pixel_y = float(px), float(py)
            self.direction = LEFT
            self.set_state(CHASE)

    def _move(self, maze, pacman, all_ghosts):
        if self._at_center():
            px, py = tile_to_pixel(self.tile_x, self.tile_y)
            self.pixel_x, self.pixel_y = float(px), float(py)
            self.tile_x, self.tile_y = wrap(self.tile_x, self.tile_y, self.cols)
            target = self.get_target(pacman, all_ghosts, maze)
            self._pick_dir(target, maze)

        self.pixel_x += self.direction[0] * self.speed
        self.pixel_y += self.direction[1] * self.speed
        self.tile_x, self.tile_y = pixel_to_tile(int(self.pixel_x), int(self.pixel_y))

    def _at_center(self):
        cx, cy = tile_to_pixel(self.tile_x, self.tile_y)
        return abs(self.pixel_x - cx) <= self.speed and abs(self.pixel_y - cy) <= self.speed

    def _pick_dir(self, target, maze):
        opp   = opposite(self.direction)
        valid = self._valid_dirs(maze, opp)
        if not valid:
            valid = self._valid_dirs(maze, None)
        if not valid:
            return

        if self.state == FRIGHTENED_STATE:
            self.direction = random.choice(valid)
            return

        best, bdist = None, float("inf")
        for d in valid:
            nx, ny = wrap(self.tile_x + d[0], self.tile_y + d[1], self.cols)
            dist = euclid_dist((nx, ny), target)
            if dist < bdist:
                bdist, best = dist, d
        if best:
            self.direction = best

    def _valid_dirs(self, maze, exclude):
        dirs = []
        for d in [UP, DOWN, LEFT, RIGHT]:
            if d == exclude:
                continue
            nx, ny = wrap(self.tile_x + d[0], self.tile_y + d[1], self.cols)
            if not maze.is_wall(nx, ny):
                if maze.is_ghost_house(nx, ny) and self.state != EATEN:
                    continue
                dirs.append(d)
        return dirs

    def get_target(self, pacman, all_ghosts, maze):
        if self.state == SCATTER:
            return self.scatter_target
        if self.state == EATEN:
            return self.house_tile
        return self.scatter_target

    def set_state(self, new):
        if self.state == EATEN and new not in (EATEN, HOUSE):
            return
        self.prev_state = self.state
        self.state      = new
        if new == FRIGHTENED_STATE:
            self.speed            = self.SPD_FRIGHTENED * TILE_SIZE / 60.0
            self.frightened_timer = POWER_UP_DURATION
            self.is_flashing      = False
            self.flash_timer      = 0
        elif new in (CHASE, SCATTER):
            self.speed       = self.SPD_NORMAL * TILE_SIZE / 60.0
            self.is_flashing = False
        elif new == EATEN:
            self.speed = self.SPD_EATEN * TILE_SIZE / 60.0

    def _frightened_tick(self, dt):
        self.frightened_timer -= dt
        if self.frightened_timer <= GHOST_FLASH_START:
            self.is_flashing  = True
            self.flash_timer += dt
            if self.flash_timer >= 250:
                self.flash_timer  = 0
                self.flash_toggle = not self.flash_toggle
        if self.frightened_timer <= 0:
            self.is_flashing = False
            self.set_state(self.prev_state)

    def _check_house(self):
        if self.tile_x == self.house_tile[0] and self.tile_y == self.house_tile[1]:
            self.dot_counter = 0
            self.set_state(CHASE)

    def increment_dot(self):
        if self.state == HOUSE:
            self.dot_counter += 1

    def get_eaten(self, combo):
        scores = {1: GHOST_SCORE_1, 2: GHOST_SCORE_2, 3: GHOST_SCORE_3, 4: GHOST_SCORE_4}
        self.eaten_score         = scores.get(combo, GHOST_SCORE_4)
        self.score_display_timer = 1000
        self.set_state(EATEN)
        return self.eaten_score

    def draw(self, screen):
        cx, cy = self.center
        if self.score_display_timer > 0:
            f = pygame.font.SysFont("arial", 14, bold=True)
            screen.blit(f.render(str(self.eaten_score), True, CYAN), (cx-10, cy-7))
            return
        if self.state == EATEN:
            self._draw_eyes(screen, cx, cy)
            return
        if self.state == FRIGHTENED_STATE:
            col = WHITE if (self.is_flashing and self.flash_toggle) else FRIGHTENED_COLOR
        else:
            col = self.color
        self._draw_body(screen, cx, cy, col)
        if self.state == FRIGHTENED_STATE:
            self._draw_scared(screen, cx, cy)
        else:
            self._draw_eyes(screen, cx, cy)

    def _draw_body(self, screen, cx, cy, col):
        r = TILE_SIZE // 2
        pygame.draw.circle(screen, col, (cx, cy - r // 4), r)
        pygame.draw.rect(screen, col, (cx - r, cy - r // 4, r * 2, r + r // 2))
        for i in range(3):
            bx = cx - r + (r // 3) + i * (r * 2 // 3)
            by = cy + r + r // 4 - (r // 6 if self.anim_frame == 0 else 0)
            pygame.draw.circle(screen, col, (bx, by), r // 3)

    def _draw_eyes(self, screen, cx, cy):
        r  = TILE_SIZE // 2
        ey = cy - r // 4
        ox, oy = self.direction[0] * 2, self.direction[1] * 2
        for s in (-1, 1):
            ex = cx + s * (r // 3)
            pygame.draw.circle(screen, WHITE, (ex, ey), r // 4)
            pygame.draw.circle(screen, BLUE, (ex + ox, ey + oy), r // 7)

    def _draw_scared(self, screen, cx, cy):
        r  = TILE_SIZE // 2
        ey = cy - r // 4
        for s in (-1, 1):
            pygame.draw.circle(screen, WHITE, (cx + s * (r // 3), ey), r // 8)
        pts = [(cx - r//2 + i*(r//6), cy + r//6 + (3 if i%2==0 else -3)) for i in range(7)]
        if len(pts) >= 2:
            pygame.draw.lines(screen, WHITE, False, pts, 2)

    def reset(self):
        self.tile_x, self.tile_y = self.start_tile
        px, py = tile_to_pixel(*self.start_tile)
        self.pixel_x, self.pixel_y = float(px), float(py)
        self.direction           = UP
        self.speed               = self.SPD_NORMAL * TILE_SIZE / 60.0
        self.state               = HOUSE
        self.prev_state          = CHASE
        self.dot_counter         = 0
        self.frightened_timer    = 0
        self.is_flashing         = False
        self.flash_toggle        = False
        self.flash_timer         = 0
        self.bounce_offset       = 0.0
        self.bounce_dir          = 1
        self.score_display_timer = 0
        self.eaten_score         = 0
        self.anim_frame          = 0
        self.anim_timer          = 0

    def __repr__(self):
        return f"<Ghost {self.name} {self.state} ({self.tile_x},{self.tile_y})>"