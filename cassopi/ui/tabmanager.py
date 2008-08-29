# -*- coding: utf-8 -*-
"""
Manager of tabs.
"""

class TabManager():
    def __init__(self):
        self.active = 0
        self.tabs = []
    
    def add(self, tab):
        self.tabs.append(tab)
    
    def render(self, tab):
        """
        Renders tabs.
        """
        # render header
        
        
        # render contents of the active tab
        self.tabs[self.active].render()
