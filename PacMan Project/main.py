import pygame
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