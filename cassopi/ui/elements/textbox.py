# -*- coding: utf-8 -*-
'''
A simple textbox containing label and entry field.
'''

suitable_values = ('name', 'value', 'tooltip', 'max_input_length', )

class TextBox():
    def __init__(self, args=None):
        if type(args) is dict:
            for suitable_value in suitable_values:
                if args.has_key(suitable_value):
                    self.__dict__[suitable_value] = args[suitable_value]
