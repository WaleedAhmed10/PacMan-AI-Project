import pygame

class ScorePopup:
    def __init__(self, value, x, y):
        self.value = value
        self.x     = x
        self.y     = float(y)
        self.timer = 1000
        self.alive = True
        self.font  = pygame.font.SysFont("arial", 14, bold=True)

    def update(self, delta_time):
        self.y     -= 0.05 * delta_time
        self.timer -= delta_time
        if self.timer <= 0:
            self.alive = False

    def is_expired(self):
        return not self.alive

    def draw(self, screen):
        surface = self.font.render(str(self.value), True, (255, 255, 255))
        screen.blit(surface, (self.x, int(self.y)))