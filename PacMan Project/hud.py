import pygame
from constants import WHITE, YELLOW, SCR_WIDTH

class HUD:
    def __init__(self):
        pygame.font.init()
        self.font_large = pygame.font.SysFont("Arial", 24)
        self.font_small = pygame.font.SysFont("Arial", 16)

    def draw(self, screen, score=0, lives=3, level=1, high_score=0):
        score_text = self.font_large.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        lives_text = self.font_small.render(f"Lives: {lives}", True, WHITE)
        screen.blit(lives_text, (10, 40))
        level_text = self.font_small.render(f"Level: {level}", True, YELLOW)
        screen.blit(level_text, (SCR_WIDTH - 120, 10))
