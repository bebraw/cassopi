# -*- coding: utf-8 -*-
"""
Sidebar of a view.
"""
from cassopi.utils.graphics.viewport import OrthoViewport

class Sidebar(object):
    def __init__(self):
        self.viewport = OrthoViewport()
    
    def render(self):
        pass
