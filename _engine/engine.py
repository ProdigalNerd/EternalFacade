from . import settings
from ._helpers import Singleton
from ._scenes import existing_scenes
from .controls import ControlManager
from .enums import EngineState

from bearlibterminal import terminal


class Engine(metaclass=Singleton):

    def __init__(self):
        self.state = EngineState.OFF
        self.control_manager = ControlManager()
        self.configure()

    # configure bearlibterminal to render the application
    def configure(self):
        # initialize the terminal to hold the game
        terminal.open()

        # set width and height of screen
        terminal.set("window.size=" + str(settings.SCREEN_W) + "x" + str(settings.SCREEN_H) + ";")
        # set application title
        terminal.set("window.title='Eternal Facade';")
        # set the size of the cells in pixels
        terminal.set("window.cellsize=8x8;")
        # set the font 'Tiles'
        terminal.set("font: " + settings.MAIN_FONT + " size=16;")
        terminal.set("0xE000: " + settings.MAIN_TILES + ", size=32x32, spacing=4x4;")

        self.state = EngineState.ON
        self.initialize_window()

    # initialize and show the game window
    def initialize_window(self):
        # TODO change in future to be state based. Use function to do so
        existing_scenes["Dungeon"].set_active(True)

        self.start_engine()

    # Set the state of the engine from outside script
    def set_state(self, state):
        self.state = state

        # TODO handle scene activation here based on new state

    # Get the current state of the engine
    def get_state(self):
        return self.state

    # Start the engine game loop
    def start_engine(self):
        while self.state != 'off':
            # set the state based on any controls that happen
            # do it this way to handle any scene changes that need to happen
            key = terminal.read()

            if key == terminal.TK_ESCAPE:
                self.set_state("off")  # exit game

            # render the active scenes
            for key, scene in existing_scenes.items():
                if scene.get_active():
                    scene.render()

            # display scenes on screen
            terminal.refresh()

            # clear the buffer for next round of rendering
            for key, scene in existing_scenes.items():
                if scene.get_active():
                    scene.clear()

        # state switched to off so close the application
        terminal.close()

    # add an object to a specific scene to be rendered
    # TODO make sure this works for the inventory scene
    def add_object_to_scene(self, obj, scene_name):
        existing_scenes[scene_name].add_object(obj)

