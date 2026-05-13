<<<<<<< HEAD
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
=======
class soundManager:
    def __init__(self):
        self.sounds = {
        "chomp"      : load_sound("chomp.wav"),
        "power_up"   : load_sound("power_pellet.wav"),
        "ghost_eat"  : load_sound("ghost_eat.wav"),
        "death"      : load_sound("pacman_death.wav"),
        "fruit"      : load_sound("fruit.wav"),
        "game_start" : load_sound("game_start.wav"),
        "extra_life" : load_sound("extra_life.wav"),
        "siren"      : load_sound("siren.wav"),
        "retreating" : load_sound("retreating.wav"),
    }
    self.siren_channel = None
    def play(self, sound_name):
        if sound_name == "siren":
            self.sounds[name].play(loops = -1 if loop else 0)
    def stop(self, sound_name):
        if sound_name == "siren" and self.siren_channel is not None:
            self.siren_channel.stop()
    def update(self, game_state):
        if game_state == "chase":
            self.play("siren")
        else:
            self.stop("siren")
            self.play("retreating")
    def load_sound(filename):
        pass
>>>>>>> c9441631f6679ee1256bd6d0941b633cc3072f25
