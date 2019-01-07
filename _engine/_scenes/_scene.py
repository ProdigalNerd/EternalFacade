from bearlibterminal import terminal


class Scene:

    def __init__(self, x, y, w, h, layer):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.layer = layer
        self.active = False

    def render(self):
        terminal.layer(self.layer)
        terminal.crop(self.x, self.y, self.w, self.h)

    def clear(self):
        terminal.layer(self.layer)
        terminal.clear_area(self.x, self.y, self.w, self.h)

    def get_active(self):
        return self.active

    def set_active(self, active):
        self.active = active

    def add_object(self, obj):
        pass
