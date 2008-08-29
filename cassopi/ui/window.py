# -*- coding: utf-8 -*-
"""
Cassopi window derived from pyglet.
"""
#from pyglet import clock, font, window
from pyglet import window
from pyglet.gl import *

class CassopiWindow(window.Window):
    def __init__(self, width=800, height=600, resizable=True, visible=True): # nicer to use vargs?
        super(CassopiWindow, self).__init__(width=width, height=height, resizable=resizable, visible=visible)
        
        # default view
        self.main_sidebar = MainSidebar()
        #self.views = [NodeView()]
    
    def on_draw(self):
        self.main_sidebar.render()
    
    def on_resize(self, width, height):
        pass
