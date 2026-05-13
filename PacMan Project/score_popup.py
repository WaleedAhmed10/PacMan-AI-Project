<<<<<<< HEAD
class ScorePopup:
=======
from utils import draw_text
class score_popup:
>>>>>>> c9441631f6679ee1256bd6d0941b633cc3072f25
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
<<<<<<< HEAD
=======
        self.timer = 1000
        self.alive = True
    def update(self, delta_time):
        self.y -= 0.05 * delta_time
        self.timer -= delta_time
        if self.timer <= 0:
            self.alive = False
    def draw(self, screen):
        draw_text(screen, str(self.value), self.x, self.y, (255, 255, 255))
>>>>>>> c9441631f6679ee1256bd6d0941b633cc3072f25
