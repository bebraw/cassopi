# -*- coding: utf-8 -*-
"""
Manager of tabs.
"""

class TabManager():
    def __init__(self, max_width):
        self.max_width = max_width
        
        self.active = 0
        self.tabs = []
    
    def add(self, tab):
        self.tabs.append(tab)
    
    def render(self, tab):
        """
        Renders tabs.
        """
        # render header
        for i, tab in enumerate(self.tabs):
            if i == self.active:
                pass # white bg
            else:
                pass # blue bg (change these later!)
            
            # render tab name
        
        # render contents of the active tab (exception, invalid index!)
        self.tabs[self.active].render()
