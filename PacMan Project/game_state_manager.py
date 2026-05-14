from constants import (CHASE, CHASE_DURATION, EATEN, GAME_OVER, HOUSE,
                       PAUSED, PLAYING, SCATTER, SCATTER_DURATION, START,
                       WIN, FRIGHTENED_STATE)
from score_popup import ScorePopup


class GameStateManager:
    def __init__(self):
        self.state         = START
        self.level         = 1
        self.high_score    = 0
        self.scatter_timer = SCATTER_DURATION
        self.chase_timer   = 0
        self.in_scatter    = True
        self.popups        = []
        self.ready_timer   = 3000

    def update(self, delta_time, pacman, ghosts, maze):
        if self.state == START:
            self.update_start_screen(delta_time)
        elif self.state == PLAYING:
            self.update_playing(delta_time, pacman, ghosts, maze)
        elif self.state == PAUSED:
            pass
        elif self.state == GAME_OVER:
            self.update_game_over(delta_time)
        elif self.state == WIN:
            self.update_win(delta_time)

    def update_start_screen(self, delta_time):
        if self.ready_timer > 0:
            self.ready_timer -= delta_time

    def update_playing(self, delta_time, pacman, ghosts, maze):
        self.update_scatter_chase(delta_time, ghosts)
        pacman.update(delta_time, maze)
        for ghost in ghosts:
            ghost.update(delta_time, pacman, maze, ghosts)
        maze.update_fruit(delta_time, maze.dots_eaten)
        self.check_all_collisions(pacman, ghosts, maze)
        for popup in self.popups[:]:
            popup.update(delta_time)
            if popup.is_expired():
                self.popups.remove(popup)

    def update_game_over(self, delta_time):
        pass

    def update_win(self, delta_time):
        pass

    def update_scatter_chase(self, delta_time, ghosts):
        if self.in_scatter:
            self.scatter_timer -= delta_time
            if self.scatter_timer <= 0:
                self.in_scatter = False
                self.chase_timer = 0
                for ghost in ghosts:
                    if ghost.state != EATEN:
                        ghost.set_state(CHASE)
        else:
            self.chase_timer += delta_time
            if self.chase_timer >= CHASE_DURATION:
                self.in_scatter    = True
                self.scatter_timer = SCATTER_DURATION
                for ghost in ghosts:
                    if ghost.state != EATEN:
                        ghost.set_state(SCATTER)

    def check_all_collisions(self, pacman, ghosts, maze):
        for ghost in ghosts:
            if (ghost.tile_x, ghost.tile_y) == (pacman.tile_x, pacman.tile_y):
                if ghost.state == FRIGHTENED_STATE:
                    score = ghost.get_eaten(pacman.ghost_combo)
                    pacman.score += score
                    pacman.ghost_combo += 1
                    self.popups.append(ScorePopup(score, ghost.tile_x, ghost.tile_y))
                elif ghost.state not in (EATEN, HOUSE):
                    pacman.lives -= 1
                    if pacman.lives <= 0:
                        self.state = GAME_OVER
                    else:
                        self.reset_positions(pacman, ghosts, maze)

    def reset_positions(self, pacman, ghosts, maze):
        pacman.reset_position()
        for ghost in ghosts:
            ghost.reset_position()

    def reset_game(self, pacman, ghosts, maze):
        self.reset_positions(pacman, ghosts, maze)
        self.ready_timer   = 3000
        self.scatter_timer = SCATTER_DURATION
        self.in_scatter    = True
        self.state         = PLAYING

    def load_next_level(self, pacman, ghosts, maze):
        maze.reset()
        pacman.reset_position()
        for ghost in ghosts:
            ghost.reset()
        self.ready_timer   = 3000
        self.scatter_timer = SCATTER_DURATION
        self.in_scatter    = True
        self.state         = PLAYING
        for ghost in ghosts:
            ghost.speed += 0.05