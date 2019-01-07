from _assets.tile_refs.misc import misc
from ._scene import Scene

from bearlibterminal import terminal


class InventoryScene(Scene):

    def __init__(self, x, y, w, h, layer):
        super().__init__(x, y, w, h, layer)

        self.emptySlot = misc.MISC_SLOT

    def render(self):
        super().render()

        y = self.y
        while y < (self.y + self.h):
            x = self.x
            while x < (self.x + self.w):
                terminal.put(x, y, self.emptySlot)
                x += 4
            y += 4
