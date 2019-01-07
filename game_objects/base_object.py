

class BaseObject:

    def __init__(self, x, y, tag, name, c):
        self.x = x
        self.y = y
        self.tag = tag
        self.name = name
        self.c = c

    def get_name(self):
        return self.name

    def get_tag(self):
        return self.tag
