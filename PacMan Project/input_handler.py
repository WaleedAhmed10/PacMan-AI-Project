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