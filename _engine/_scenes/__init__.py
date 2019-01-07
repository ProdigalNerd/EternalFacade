from _engine import settings

from .dungeon_scene import DungeonScene
from .player_info_scene import PlayerInfoScene
from .inventory_scene import InventoryScene

existing_scenes = {
    "Dungeon": DungeonScene(0, 0, settings.DUNGEON_WIDTH, settings.DUNGEON_HEIGHT, 1),
    "PlayerInfo": PlayerInfoScene(settings.DUNGEON_WIDTH, 0, settings.SI_WIDTH, settings.SI_HEIGHT, 2),
    "Inventory": InventoryScene(settings.DUNGEON_WIDTH, settings.SI_HEIGHT, settings.INV_WIDTH, settings.INV_HEIGHT, 3)
}
