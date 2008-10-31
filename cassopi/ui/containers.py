from elements import TextBox, ToggleButton
from paddings import Padding

class AbstractContainer():
    def __init__(self, padding=None, args=None):
        self.padding = Padding(padding) if type(padding) is dict else padding
        self.children = []
        
        if type(args) is dict:
            if args.has_key('padding'):
                self.padding = Padding(args['padding'])
            if args.has_key('children'):
                for child in args['children']:
                    self.children.append(globals()[child.keys()[0]](args=child.values()[0]))

class HorizontalContainer(AbstractContainer):
    pass

class VerticalContainer(AbstractContainer):
    pass
