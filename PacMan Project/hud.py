from constraints import RIGHT, RIGHT, WHITE


class hud:
    def __init__(self, font_large, font_small, icon):
        self.font_large = load_font("arcade.ttf", size=24)
        self.font_small = load_font("arcade.ttf", size=16)
        self.icon = load_image("icon.png")
    def draw(self, score, lives):
        draw_text(f"Score: {score}", self.font_large, (255, 255, 255), 10, 10)
        draw_text(f"Lives: {lives}", self.font_small, (255, 255, 255), 10, 40)
        draw_image(self.icon, 10, 70)
        draw_text(screen, "HIGH SCORE", pos=(CENTER_X, 5),  color=WHITE, font=self.font_small)
        draw_text(screen, f"{high_score}", pos=(CENTER_X, 30), color=WHITE, font=self.font_large)
        draw_text(screen, f"LV {level}", pos=(RIGHT-60, 20), color=YELLOW, font=self.font_large)
        for i in range(lives):
            draw_image(self.life_icon, (RIGHT - 30) - (i * 30), 20)
        for i, fruit in enumerate(fruits):
            draw_fruit_icon(screen, fruit, pos=(SCREEN_WIDTH - 20 - i * 20, SCREEN_HEIGHT - 20))