from maps.base_map import BaseMap
from maps.forest_configs import configs

import random


class ForestMap(BaseMap):

    def __init__(self, seed):
        super().__init__(seed)

        self.config = configs[random.randint(0, len(configs) - 1)]

    def initialize_map(self):
        return super().initialize_map()

