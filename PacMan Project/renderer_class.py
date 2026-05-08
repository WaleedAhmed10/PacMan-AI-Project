from turtle import fill
from constraints import BLACK, GAME_OVER, WIN
import pygame

class renderer:
    def __init__ (self, screen):
        self.screen = screen
    def draw_all(self, maze, pacman, ghosts, hud, popups, game_state, ready_timer):
        fill(self.screen, BLACK)
        maze.draw(self.screen)
        pacman.draw(self.screen)
        for ghost in ghosts:
            ghost.draw(self.screen)
        for popup in popups:
            popup.draw(self.screen)
            hud.draw(self.screen, pacman, current_level, high_score)
            if game_state == "PAUSED":
                draw_centered_text(self.screen, "PAUSED", 60)
            if ready_timer > 0:
                draw_centered_text(self.screen, "READY", 60)
            if game_state == GAME_OVER:
                draw_centered_text(self.screen, "GAME OVER", color=RED, y=CENTER_Y)
            if game_state == WIN:
                draw_centered_text(self.screen, "YOU WIN!", color=YELLOW, y=CENTER_Y)
            pygame.display.flip()