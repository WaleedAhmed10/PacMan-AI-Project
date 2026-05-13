from constraints import START, PLAYING, PAUSED, GAME_OVER

class GameStateManager:
    def __init__(self):
        self.state = START
        self.level = 1
        self.running = True
        self.popups = []
        self.ready_timer = 3000

    def update(self, delta_time):
        return self.state

    def restart(self):
        self.state = START
        self.level = 1
