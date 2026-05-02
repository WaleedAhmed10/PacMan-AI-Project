class animation:
    def __init__(self, frames, frame_duration, loop=True):
        self.frames = frames
        self.frame_duration = frame_duration
        self.timer = 0
        self.current_frame = 0
        self.loop = loop
        self.done = False
    def update(self, delta_time):
        self.timer += delta_time
        if self.timer >= self.frame_duration:
            self.timer = 0
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                if self.loop:
                    self.current_frame = 0
                else:
                    self.current_frame = len(self.frames) - 1
                    self.done = True
    def get_current_frame(self):
        return self.frames[self.current_frame]
    def reset(self):
        self.timer = 0 
        self.current_frame = 0
        self.done = False