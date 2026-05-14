import pygame
from constants import GAME_OVER, PAUSED, PLAYING, START, UP, DOWN, LEFT, RIGHT


class InputHandler:
    def handle_events(self, game_state_manager, pacman, sound=None):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state_manager.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    pacman.next_direction = UP
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    pacman.next_direction = DOWN
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    pacman.next_direction = LEFT
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    pacman.next_direction = RIGHT
                elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                    if game_state_manager.state == PLAYING:
                        game_state_manager.state = PAUSED
                    elif game_state_manager.state == PAUSED:
                        game_state_manager.state = PLAYING
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    if game_state_manager.state == START:
                        game_state_manager.state = PLAYING
                    elif game_state_manager.state == GAME_OVER:
                        game_state_manager.restart()
                elif event.key == pygame.K_m and sound:
                    sound.toggle_mute()