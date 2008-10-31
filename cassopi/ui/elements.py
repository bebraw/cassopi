# -*- coding: utf-8 -*-

class AbstractElement(object):
    def __init__(self, args=None):
        self.find_values(args)
    
    def check_arg(self, dict, arg):
        if dict.has_key(arg):
            return dict[arg]
    
    def find_values(self, args):
        if type(args) is dict:
            for suitable_value in self.suitable_values:
                self.__dict__[suitable_value] = self.check_arg(args, suitable_value)

class TextBox(AbstractElement):
    suitable_values = ('name', 'value', 'tooltip', 'max_input_length', )

class ToggleButton(AbstractElement):
    suitable_values = ('name', 'value', 'tooltip', )
