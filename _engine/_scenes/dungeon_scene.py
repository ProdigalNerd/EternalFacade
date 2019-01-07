from _engine import settings
from ._scene import Scene

import maps

import random

from bearlibterminal import terminal


class DungeonScene(Scene):

    def __init__(self, x, y, w, h, layer):
        super().__init__(x, y, w, h, layer)
        self.map = self.go_to_level(1)
        self.player = {"dx": 0, "dy": 0}

        # TODO fix this temporary map fix
        self.player["dy"] = (self.h // 2)
        self.player["dx"] = (self.w // 2)

        self.objects = []

    def add_object(self, obj):
        super().add_object(obj)

        if hasattr(obj, 'tag') and obj.get_tag() == 'player':
            self.add_player_to_scene(obj)
        else:
            self.objects.append(obj)

    def add_player_to_scene(self, player):
        self.player = player
        self.map = self.go_to_level(1)
        self.objects.append(player)

    def render(self):
        super().render()

        self.render_map()

        terminal.composition(terminal.TK_ON)
        for obj in self.objects:
            terminal.put(obj.x, obj.y, obj.c)
        terminal.composition(terminal.TK_OFF)

    def render_map(self):
        if self.map:
            y = 0
            while y < self.h:
                x = 0
                while x < self.w:
                    # need the x/y coordinates for the tile relative to the players dungeon location
                    # not where the tile will be placed
                    y_index = self.player["dy"] - (self.h // 2) + (y // settings.DUNGEON_TILE_SIZE)
                    x_index = self.player["dx"] - (self.w // 2) + (x // settings.DUNGEON_TILE_SIZE)

                    # create a tuple to compare with the map
                    coord = x_index, y_index

                    # check that there is a tile to be rendered within the bounds of the map object
                    # this prevents the rendering of the same map showing multiple times recursively
                    if coord in self.map:
                        terminal.composition(terminal.TK_ON)
                        for tile in self.map[coord]:
                            if tile:
                                terminal.put(x, y, tile)
                        terminal.composition(terminal.TK_OFF)

                    x += settings.DUNGEON_TILE_SIZE
                y += settings.DUNGEON_TILE_SIZE

    def go_to_level(self, lvl):
        # set the random seed
        # TODO Fix this pls
        # seed = self.player.name

        # filter to only check for maps available at the level the player is on
        possible_maps = [m for m in maps.maps if m[1] <= lvl >= m[2]]

        selected_map = None

        # make sure there were maps found before trying to create it
        if len(possible_maps) > 0:
            # pick a random map that is allowed on that level
            gen_map = possible_maps[random.randint(0, len(possible_maps) - 1)]

            # initialize the map class
            selected_map = gen_map[0](1)

        return selected_map.initialize_map()
