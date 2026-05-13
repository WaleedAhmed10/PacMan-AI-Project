import pygame
from constants import SCR_WIDTH, SCR_HEIGHT, FPS
from game_state_manager import GameStateManager
from input_handler import InputHandler
from renderer_class import Renderer
from hud import HUD

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption("Pac-Man AI Project")
    clock = pygame.time.Clock()

    gsm = GameStateManager()
    input_handler = InputHandler()
    renderer = Renderer(screen)
    hud = HUD()

    class DummyPacman:
        direction = "right"

    pacman = DummyPacman()

    while gsm.running:
        input_handler.handle_events(gsm, pacman)
        renderer.draw_all(None, pacman, [], hud, [], gsm.state, gsm.ready_timer)
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
