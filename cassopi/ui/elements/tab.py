# -*- coding: utf-8 -*-
"""
Tab of a sidebar. (restrict to sidebars?)
"""
from element import Element

class Tab(Element):
    def __init__(self, name):
        super(Tab, self).__init__(name)
        self.elements = []
        # how to handle event? -> ie. user clicks tab header -> context switch. scrollbars???
    
    def add(self, element):
        self.elements.append(element)
    
    def render(self):
        """
        Render contents of tab (doesn't include tab name!).
        """
        pass
