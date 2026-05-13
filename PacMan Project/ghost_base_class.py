class ghost:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name", "Ghost")

    def draw(self, screen):
        return None
