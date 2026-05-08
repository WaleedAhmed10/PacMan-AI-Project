import pygame
import math
from constants import *

def tile_to_pixel(tx, ty):
    return (tx * TILE_SIZE + TILE_SIZE // 2, ty * TILE_SIZE + TILE_SIZE // 2)
def pixel_to_tile(px, py):
    return px // TILE_SIZE, py // TILE_SIZE
def wrap(tx, ty, cols):
    if tx < 0: tx = cols - 1
    elif tx >= cols: tx = 0
    return tx, ty
class PacMan:
    SPD_NORMAL  = 2.0
    SPD_POWERED = 2.2
    def __init__(self, start_tile, cols):
        self.start_tile = start_tile
        self.cols       = cols
        self.tile_x, self.tile_y = start_tile
        px, py = tile_to_pixel(*start_tile)
        self.pixel_x, self.pixel_y = float(px), float(py)
        self.direction      = LEFT
        self.next_direction = LEFT
        self.speed          = self.SPD_NORMAL * TILE_SIZE / 60.0
        self.lives       = 3
        self.score       = 0
        self.powered_up  = False
        self.power_timer = 0
        self.ghost_combo = 0
        self.alive            = True
        self.death_timer      = 0
        self.death_duration   = 1200
        self.mouth_angle  = 45
        self.mouth_closing= True
        self.anim_timer   = 0
    @property
    def center(self):
        return (int(self.pixel_x), int(self.pixel_y))
    @property
    def tile(self):
        return (self.tile_x, self.tile_y)
    def update(self, dt, maze):
        if not self.alive:
            self.death_timer += dt
            return
        self._update_power(dt)
        self._update_mouth(dt)
        self._move(maze)
        self._eat(maze)

    def _move(self, maze):
        if self._at_center():
            px, py = tile_to_pixel(self.tile_x, self.tile_y)
            self.pixel_x, self.pixel_y = float(px), float(py)
            self.tile_x, self.tile_y = wrap(self.tile_x, self.tile_y, self.cols)

            if self._can_move(self.next_direction, maze):
                self.direction = self.next_direction
            if not self._can_move(self.direction, maze):
                return
            self.tile_x += self.direction[0]
            self.tile_y += self.direction[1]
            self.tile_x, self.tile_y = wrap(self.tile_x, self.tile_y, self.cols)
        self.pixel_x += self.direction[0] * self.speed
        self.pixel_y += self.direction[1] * self.speed

    def _at_center(self):
        cx, cy = tile_to_pixel(self.tile_x, self.tile_y)
        return abs(self.pixel_x - cx) <= self.speed and abs(self.pixel_y - cy) <= self.speed

    def _can_move(self, d, maze):
        nx = self.tile_x + d[0]
        ny = self.tile_y + d[1]
        nx, ny = wrap(nx, ny, self.cols)
        return not maze.is_wall(nx, ny) and not maze.is_ghost_house(nx, ny)

    def _eat(self, maze):
        tile = maze.get_tile(self.tile_x, self.tile_y)
        if tile == DOT:
            self.score += DOT_SCORE
            maze.set_tile(self.tile_x, self.tile_y, EMPTY)
            maze.dots_eaten += 1
        elif tile == POWER_PELLET:
            self.score      += POWER_PELLET_SCORE
            self.powered_up  = True
            self.power_timer = POWER_UP_DURATION
            self.ghost_combo = 0
            self.speed       = self.SPD_POWERED * TILE_SIZE / 60.0
            maze.set_tile(self.tile_x, self.tile_y, EMPTY)
            maze.dots_eaten += 1

    def _update_power(self, dt):
        if self.powered_up:
            self.power_timer -= dt
            if self.power_timer <= 0:
                self.powered_up  = False
                self.ghost_combo = 0
                self.speed       = self.SPD_NORMAL * TILE_SIZE / 60.0

    def _update_mouth(self, dt):
        self.anim_timer += dt
        if self.anim_timer >= 50:
            self.anim_timer = 0
            if self.mouth_closing:
                self.mouth_angle -= 5
                if self.mouth_angle <= 0:
                    self.mouth_closing = False
            else:
                self.mouth_angle += 5
                if self.mouth_angle >= 45:
                    self.mouth_closing = True

    def eat_ghost(self):
        self.ghost_combo += 1
        scores = {1: GHOST_SCORE_1, 2: GHOST_SCORE_2,
                  3: GHOST_SCORE_3, 4: GHOST_SCORE_4}
        bonus = scores.get(self.ghost_combo, GHOST_SCORE_4)
        self.score += bonus
        return bonus

    def lose_life(self):
        self.lives      -= 1
        self.alive       = False
        self.death_timer = 0

    def death_done(self):
        return not self.alive and self.death_timer >= self.death_duration

    def reset(self):
        self.tile_x, self.tile_y = self.start_tile
        px, py = tile_to_pixel(*self.start_tile)
        self.pixel_x, self.pixel_y = float(px), float(py)
        self.direction      = LEFT
        self.next_direction = LEFT
        self.speed          = self.SPD_NORMAL * TILE_SIZE / 60.0
        self.powered_up     = False
        self.power_timer    = 0
        self.ghost_combo    = 0
        self.alive          = True
        self.death_timer    = 0
        self.mouth_angle    = 45
        self.mouth_closing  = True
        self.anim_timer     = 0

    def draw(self, screen):
        cx, cy = self.center
        r = TILE_SIZE // 2

        if not self.alive:
            progress = min(self.death_timer / self.death_duration, 1.0)
            angle = int(360 * progress)
            if angle < 360:
                pygame.draw.circle(screen, YELLOW, (cx, cy), r)
                pygame.draw.polygon(screen, BLACK, [ (cx, cy), (cx + r * math.cos(math.radians(-angle // 2))),
                    (cy + r * math.sin(math.radians(-angle // 2))), (cx + r, cy) ])
            return

        dir_angles = {
            RIGHT: 0, LEFT: 180, UP: 90, DOWN: 270
        }
        base = dir_angles.get(self.direction, 0)
        start_a = math.radians(base + self.mouth_angle)
        end_a   = math.radians(base - self.mouth_angle)
        points = [(cx, cy)]
        steps  = 30
        for i in range(steps + 1):
            t = i / steps
            a = start_a + t * (end_a - start_a + 2 * math.pi) % (2 * math.pi)
            a = start_a + t * ((end_a - start_a) % (2 * math.pi))
            points.append((
                cx + r * math.cos(a),
                cy - r * math.sin(a)
            ))

        if len(points) >= 3:
            pygame.draw.polygon(screen, YELLOW, points)