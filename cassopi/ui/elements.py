# -*- coding: utf-8 -*-

class AbstractElement():
    def __init__(self, args=None):
        self.find_values(args)
    
    def find_values(self):
        if type(args) is dict:
            for suitable_value in self.suitable_values:
                if args.has_key(suitable_value):
                    self.__dict__[suitable_value] = args[suitable_value]

class TextBox(AbstractElement):
    suitable_values = ('name', 'value', 'tooltip', 'max_input_length', )

class ToggleButton():
    suitable_values = ('name', 'value', 'tooltip', )
