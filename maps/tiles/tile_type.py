from enum import Enum


class TileType(Enum):
    FLOOR = 0
    WALL = 1
    DECORATION = 2
    UPSTAIRS = 3
    DOWNSTAIRS = 4
    EMPTY = 5
