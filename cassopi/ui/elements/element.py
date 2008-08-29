# -*- coding: utf-8 -*-
"""
Base class of all user interface elements.
"""

class Element(object):
    def __init__(self, name=None, event=None):
        self.name = name
        self.event = event
    
    def render(self):
        pass
