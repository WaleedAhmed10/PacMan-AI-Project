import pygame
from constants import BLACK

class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_all(self, maze, pacman, ghosts, hud, popups, game_state, ready_timer):
        self.screen.fill(BLACK)
        pygame.display.flip()
