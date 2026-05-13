import pygame
from constraints import GAME_OVER, PAUSED, PLAYING, START

class InputHandler:
    def handle_events(self, game_state_manager, pacman, sound=None):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state_manager.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    pacman.direction = 'up'
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    pacman.direction = 'down'
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    pacman.direction = 'left'
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    pacman.direction = 'right'
                elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                    game_state_manager.state = PAUSED if game_state_manager.state == PLAYING else PLAYING
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    if game_state_manager.state == START:
                        game_state_manager.state = PLAYING
                    elif game_state_manager.state == GAME_OVER:
                        game_state_manager.restart()
                elif event.key == pygame.K_m and sound:
                    sound.toggle_mute()
