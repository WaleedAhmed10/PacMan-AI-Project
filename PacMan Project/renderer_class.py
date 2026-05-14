import pygame
from constants import BLACK, GAME_OVER, WIN, WHITE, YELLOW, RED, SCR_WIDTH, SCR_HEIGHT, PAUSED

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.SysFont("arial", 60, bold=True)
        self.font_small = pygame.font.SysFont("arial", 36)

    def draw_all(self, maze, pacman, ghosts, hud, popups, game_state, ready_timer):
        self.screen.fill(BLACK)
        maze.draw(self.screen)
        pacman.draw(self.screen)
        for ghost in ghosts:
            ghost.draw(self.screen)
        for popup in popups:
            popup.draw(self.screen)
        hud.draw(self.screen)
        if game_state == PAUSED:
            self._draw_centered_text("PAUSED", self.font_large, WHITE)
        if ready_timer > 0:
            self._draw_centered_text("READY!", self.font_large, YELLOW)
        if game_state == GAME_OVER:
            self._draw_centered_text("GAME OVER", self.font_large, RED)
        if game_state == WIN:
            self._draw_centered_text("YOU WIN!", self.font_large, YELLOW)
        pygame.display.flip()

    def _draw_centered_text(self, text, font, color):
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=(SCR_WIDTH // 2, SCR_HEIGHT // 2))
        self.screen.blit(surface, rect)