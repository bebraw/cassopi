class AbstractContainer():
    def __init__(self, padding=None):
        self.padding = padding
        self.children = []

class HorizontalContainer(AbstractContainer):
    pass

class VerticalContainer(AbstractContainer):
    pass
