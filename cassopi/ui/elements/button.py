# -*- coding: utf-8 -*-
"""
Simple button.
"""
from element import Element

class Button(Element):
    def __init__(self, name, event=None):
        super(Button, self).__init__(name, event)
    
    def render(self):
        pass # should render as buttonish (corner bevels!)
