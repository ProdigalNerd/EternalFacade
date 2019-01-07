from maps.tiles import TileType

import random


class BaseMap:

    def __init__(self, seed):
        # set up the seed for the random number generator
        random.seed(seed)

        # base setup for the config object
        self.config = {}

    def new_grid_array(self, w, h):
        # creates a dictionary with the key being a tuple of x-y coordinates and the value the TileType used
        dict = {}
        for y in range(h):
            for x in range(w):
                key = x, y
                dict[key] = TileType.FLOOR

        return dict

    def render_map(self, grid):
        # Convert the Tile Type into a graphical tile
        for coord, tile in grid.items():
            if grid[coord] == TileType.EMPTY and self.config["fill_empty"]:
                grid[coord] = TileType.WALL

            if grid[coord] == TileType.EMPTY:
                # need consistency for the tuple so add None when only one ascii character is used
                grid[coord] = (' ', None)
            elif grid[coord] == TileType.FLOOR:
                # need consistency for the tuple so add None when only one ascii character is used
                grid[coord] = (random.choice(self.config["f_tiles"]), None)
            elif grid[coord] == TileType.WALL:
                # wall tiles sometimes overlap the ground. Need to have both tiles ready a composite tile.
                grid[coord] = (random.choice(self.config["f_tiles"]), random.choice(self.config["w_tiles"]))

    def process_extras(self):
        pass

    def initialize_map(self):
        # now that the config is set we can create the base map array
        grid = self.new_grid_array(w=self.config['max_x'], h=self.config['max_y'])

        # initialize the var that will hold the selected generator class
        gen_class = None

        # based on the config, import the class used to generate the map
        if self.config['gen_type'] == 'automata':
            gen_class = getattr(__import__('_generators'), 'cellular_automata')

        # all generators share the same constructor so this is safe
        grid = gen_class.generate_grid(grid, self.config['max_x'], self.config['max_y'])

        self.process_extras()

        self.render_map(grid)

        return grid
