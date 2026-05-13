class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.muted = False

    def play(self, sound_name, loop=False):
        return None

    def stop(self, sound_name):
        return None

    def toggle_mute(self):
        self.muted = not self.muted
