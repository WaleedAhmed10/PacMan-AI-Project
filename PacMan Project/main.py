import pygame
from constants import SCR_WIDTH, SCR_HEIGHT, FPS, PLAYING, EATEN
from game_state_manager import GameStateManager
from input_handler import InputHandler
from renderer_class import Renderer
from hud import HUD
from maze_class import Maze
from maze_layout import MAZE_GRID
from ghost_subclass import Blinky, Pinky, Inky, Clyde
from soundManager import SoundManager


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption("Pac-Man")
    clock = pygame.time.Clock()
    maze   = Maze(MAZE_GRID)
    blinky = Blinky()
    pinky  = Pinky()
    inky   = Inky()
    clyde  = Clyde()
    ghosts = [blinky, pinky, inky, clyde]
    gsm           = GameStateManager()
    hud           = HUD()
    renderer      = Renderer(screen)
    sound         = SoundManager()
    input_handler = InputHandler()

    class DummyPacman:
        tile_x      = 20
        tile_y      = 23
        pixel_x     = 20 * 32 + 16
        pixel_y     = 23 * 32 + 16
        direction   = (1, 0)
        next_direction = (1, 0)
        score       = 0
        lives       = 3
        ghost_combo = 0
        def update(self, dt, maze): pass
        def draw(self, screen): pass
        def reset_position(self): pass

    pacman = DummyPacman()
    while gsm.running:
        dt = clock.tick(FPS)
        input_handler.handle_events(gsm, pacman, sound)
        if gsm.state == PLAYING:
            gsm.update(dt, pacman, ghosts, maze)
        renderer.draw_all(maze, pacman, ghosts, hud, gsm.popups, gsm.state, gsm.ready_timer)
    pygame.quit()

if __name__ == "__main__":
    main()