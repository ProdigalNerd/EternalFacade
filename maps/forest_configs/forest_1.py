from _assets.tile_refs.dungeon.floor.grass import grass
from _assets.tile_refs.dungeon.trees import trees

FOREST_CONFIG_1 = {
    "name": "Forest",
    "f_tiles": [
        grass.GRASS_GRASS_0_NEW,
        grass.GRASS_GRASS_0_OLD,
        grass.GRASS_GRASS_1_NEW,
        grass.GRASS_GRASS_1_OLD,
        grass.GRASS_GRASS_2_NEW,
        grass.GRASS_GRASS_2_OLD,
        grass.GRASS_GRASS_FLOWERS_BLUE_1_NEW,
        grass.GRASS_GRASS_FLOWERS_BLUE_1_OLD,
        grass.GRASS_GRASS_FLOWERS_BLUE_2_NEW,
        grass.GRASS_GRASS_FLOWERS_BLUE_2_OLD,
        grass.GRASS_GRASS_FLOWERS_BLUE_3_NEW,
        grass.GRASS_GRASS_FLOWERS_BLUE_3_OLD,
        grass.GRASS_GRASS_FLOWERS_RED_1_NEW,
        grass.GRASS_GRASS_FLOWERS_RED_1_OLD,
        grass.GRASS_GRASS_FLOWERS_RED_2_NEW,
        grass.GRASS_GRASS_FLOWERS_RED_2_OLD,
        grass.GRASS_GRASS_FLOWERS_RED_3_NEW,
        grass.GRASS_GRASS_FLOWERS_RED_3_OLD,
        grass.GRASS_GRASS_FLOWERS_YELLOW_1_NEW,
        grass.GRASS_GRASS_FLOWERS_YELLOW_1_OLD,
        grass.GRASS_GRASS_FLOWERS_YELLOW_2_NEW,
        grass.GRASS_GRASS_FLOWERS_YELLOW_2_OLD,
        grass.GRASS_GRASS_FLOWERS_YELLOW_3_NEW,
        grass.GRASS_GRASS_FLOWERS_YELLOW_3_OLD,
    ],
    "w_tiles": [
        trees.TREES_MANGROVE_1,
        trees.TREES_MANGROVE_2,
        trees.TREES_MANGROVE_3,
        trees.TREES_TREE_1_LIGHTRED,
        trees.TREES_TREE_1_RED,
        trees.TREES_TREE_1_YELLOW,
        trees.TREES_TREE_2_LIGHTRED,
        trees.TREES_TREE_2_RED,
        trees.TREES_TREE_2_YELLOW
    ],
    "d_tiles": [

    ],
    "t_tiles": [

    ],
    "gen_type": "automata",
    "max_x": 250,
    "max_y": 250,
    "level_min": 0,
    "level_max": 1,
    "biome": "forest",
    "random": True,
    "fill_empty": True,
    "layouts": [],
    "control_keys": []
}