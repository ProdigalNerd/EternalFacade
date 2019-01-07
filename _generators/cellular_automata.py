from maps.tiles import TileType

import random
import memory_profiler


def check_tile_match(tile, coord, map_ref):
    min_x = coord[0] - 1
    max_x = coord[0] + 1
    min_y = coord[1] - 1
    max_y = coord[1] + 1

    num_adj = 0
    num_diag = 0

    for cy in range(min_y, max_y + 1):
        for cx in range(min_x, max_x + 1):
            # pack coords to check into tuple
            key = cx, cy

            # check if that key exists in the grid
            if key not in map_ref:
                continue

            # check if comparing with the tile being evaluated
            if cx == coord[0] and cy == coord[1]:
                continue

            # check if the tile matches the type we are looking for
            if map_ref[key] == tile:
                if cx == coord[0] or cy == coord[1]:
                    num_adj += 1
                else:
                    num_diag += 1

    return num_adj, num_diag


def generate_grid(base_map, max_h, max_w):
    # probability that a wall will be added
    init_wall_prob = 45
    # number of generations the cells will go through
    num_generations = 8

    # create a clone of the map to make changes to
    new_map = base_map
    map_clone = base_map

    # Place random walls
    for coord, tile in new_map.items():
        rnd = random.randint(0, 100)

        if rnd <= init_wall_prob:
            map_clone[coord] = TileType.WALL
        else:
            map_clone[coord] = TileType.FLOOR

    new_map = map_clone

    # based on generation settings iterate over the cells to expand into more of a map
    for g in range(0, num_generations):
        for coord, tile in new_map.items():
            if coord[0] == 0 or coord[0] == max_w - 1 or coord[1] == 0 or coord[1] == max_h - 1:
                map_clone[coord] = TileType.WALL
            else:
                num_walls = check_tile_match(TileType.WALL, coord, new_map)
                adj = num_walls[0]
                diag = num_walls[1]
                current = new_map[coord]

                if (adj + diag) > 4:
                    map_clone[coord] = TileType.WALL
                elif (adj + diag) < 4:
                    map_clone[coord] = TileType.FLOOR
                else:
                    map_clone[coord] = current

        new_map = map_clone

    return new_map
