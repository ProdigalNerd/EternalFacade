from ._scene import Scene

from bearlibterminal import terminal


class PlayerInfoScene(Scene):

    def __init__(self, x, y, w, h, layer):
        super().__init__(x, y, w, h, layer)
        self.player = {}

    def set_player(self, player):
        self.player = player

    def render(self):
        super().render()

        terminal.printf(self.x + 1, self.y + 1, self.player.name)
