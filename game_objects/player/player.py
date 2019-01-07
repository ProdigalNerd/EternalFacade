from _helpers.Singleton import Singleton
from _scenes.dungeon_scene import DungeonScene
from _scenes.player_info_scene import PlayerInfoScene
from game_objects.base_object import BaseObject


class Player(BaseObject, metaclass=Singleton):

    def __init__(self, x, y, tag, name, c):
        super().__init__(x, y, tag, name, c)

        # x coordinate in the dungeon
        self.dx = x
        # y coordinate in the dungeon
        self.dy = y

        # add this object to the dungeon scene
        dungeon = DungeonScene()
        dungeon.add_player_to_scene(self)

        # add this object to the stat/info scene
        player_info = PlayerInfoScene()
        player_info.set_player(self)

    def move(self, x, y):
        # don't move the players rendered position, but update the reference to their location within the dungeon map
        self.dx += x
        self.dy += y

