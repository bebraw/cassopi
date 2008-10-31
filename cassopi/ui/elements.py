# -*- coding: utf-8 -*-

class AbstractElement(object):
    def __init__(self, args=None):
        self.find_values(args)
    
    def find_values(self, args):
        if type(args) is dict:
            for suitable_value in self.suitable_values:
                if args.has_key(suitable_value):
                    self.__dict__[suitable_value] = args[suitable_value]

class TextBox(AbstractElement):
    suitable_values = ('name', 'value', 'tooltip', 'max_input_length', )
    
    def __init__(self, args=None):
        super(TextBox, self).__init__(args)

class ToggleButton(AbstractElement):
    suitable_values = ('name', 'value', 'tooltip', )
    
    def __init__(self, args=None):
        super(ToggleButton, self).__init__(args)
