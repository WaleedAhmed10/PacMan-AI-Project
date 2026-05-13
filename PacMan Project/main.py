import pygame
<<<<<<< HEAD
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
=======
def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption("Pac-Man")
    clock = pygame.time.Clock()
    maze    = Maze(MAZE_GRID)
    pacman  = PacMan(START_TILE_X, START_TILE_Y)
    blinky  = Blinky()
    pinky   = Pinky()
    inky    = Inky()
    clyde   = Clyde()
    ghosts  = [blinky, pinky, inky, clyde]
    gsm     = GameStateManager()
    input_h = InputHandler()
    hud = HUD()
    renderer = Renderer(screen)
    sound = SoundManager()
    
    while gsm.state != GameState.QUIT:
        dt = clock.tick(FPS)
        input_h.handle_events(gsm)
        if gsm.state == GameState.PLAYING:
            pacman.update(dt, maze, ghosts, sound)
            for ghost in ghosts:
                ghost.update(dt, maze, pacman)
            gsm.check_collisions(pacman, ghosts, sound)
        renderer.render(maze, pacman, ghosts, hud)
    save_high_score(gsm.high_score)
    pygame.quit()
    if __name__ == "__main__":
        main()
>>>>>>> c9441631f6679ee1256bd6d0941b633cc3072f25
