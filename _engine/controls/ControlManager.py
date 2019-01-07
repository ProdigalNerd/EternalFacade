from bearlibterminal import terminal

# TODO decide if singleton is needed
# TODO evaluate if this class is even needed -- leaning towards not needing it

class ControlManager:

    def __init__(self):
        # maybe pass a config into this to customize object actions?
        pass

    def handle_controls(self, current_state):
        # state to update on the engine
        return_state = current_state

        key = terminal.read()

        if key == terminal.TK_ESCAPE:
            return_state = "off"  # exit game

        return return_state
