from maps.tiles import TileType


class BaseGenerator:

    def __init__(self, base_map):
        # bring in the default array to maintain size of grid
        self.map_grid = base_map

    def generate_grid(self):
        pass

    def copy_grid(self):
        return [[TileType.FLOOR for c in range(0, len(self.map_grid[0]))] for r in range(0, len(self.map_grid))]

    def check_tile_match(self, t_type, x, y):
        # basic grid
        min_x = x - 1
        max_x = x + 1
        min_y = y - 1
        max_y = y + 1

        # make adjustments if it is on the edge
        if x <= 0:
            min_x = 0

        if y <= 0:
            min_x = 0

        if x >= len(self.map_grid[0]) - 1:
            max_x = len(self.map_grid[0]) - 1

        if y >= len(self.map_grid) - 1:
            max_y = len(self.map_grid) - 1

        num_adj = 0
        num_diag = 0

        for cy in range(min_y, max_y + 1):
            for cx in range(min_x, max_x + 1):
                # skip if it is the tile being evaluated
                if cx == x and cy == y:
                    pass
                elif self.map_grid[cy][cx] == t_type:
                    # determine if adjacent or diagonal
                    if cx == x or cy == y:
                        num_adj += 1
                    else:
                        num_diag += 1

        # return tuple containing (num_adj, num_diag)
        return num_adj, num_diag
