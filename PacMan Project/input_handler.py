<<<<<<< HEAD
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
=======
from json.encoder import ESCAPE
from constraints import GAME_OVER, PAUSED, PLAYING, START


class inputHandler:
    def handle_events(self, game_state_manager, pacman):
        for event in game_state_manager.events:
            if event.type == game_state_manager.QUIT:
                game_state_manager.running = False
            elif event.type == game_state_manager.KEYDOWN:
                if event.key == game_state_manager.K_UP:
                    pacman.direction = 'up' or pacman.direction = 'W'
                elif event.key == game_state_manager.K_DOWN:
                    pacman.direction = 'down' or pacman.direction = 'S'
                elif event.key == game_state_manager.K_LEFT:
                    pacman.direction = 'left' or pacman.direction = 'A'
                elif event.key == game_state_manager.K_RIGHT:
                    pacman.direction = 'right' or pacman.direction = 'D'
            if event.key == ESCAPE or event.key == game_state_manager.K_q:
                if game_state_manager.state == PLAYING:
                    game_state_manager.state = PAUSED
                elif game_state_manager.state == PAUSED:
                    game_state_manager.state = PLAYING
            if event.key == ENTER or event.key == game_state_manager.SPACE:
                if game_state_manager.state == START:
                    game_state_manager.state = PLAYING
                elif game_state_manager.state == GAME_OVER:
                    game_state_manager.restart()
                if event.key == game_state_manager.K_m: sound.toggle_mute()
>>>>>>> c9441631f6679ee1256bd6d0941b633cc3072f25
