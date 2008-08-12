# -*- coding: utf-8 -*-
from pyglet import app, clock, font, window
from pyglet.gl import *

from colorutils import *
from drawutils import *
from mathutils import *
from viewport import *

'''
TODO:
-clean up drawing and convert to classes (add texture support?)
-convert viewports to use KD scheme!!!
-add more ui stuff (events, possibility to resize, split, remove)
-ui controls (subwindows)
'''

class AppWindow(window.Window):
    def __init__(self, width=800, height=600, resizable=True, visible=True):
        super(AppWindow, self).__init__(width=width, height=height, resizable=resizable, visible=visible)
        
        self.rtri = 0.0
        self.rquad = 0.0
        clock.schedule_interval(self.update, 0.01)
        
        self.label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=100, y=100,
                          anchor_x='center', anchor_y='center')
        
        self.viewports = [] # pretty dumb atm. just store bg color (used only in ortho view)
        
        self.viewports.append(OrthoViewport(0, self.height / 2, self.width / 2, self.height, ORANGE))
        self.viewports.append(PerspectiveViewport(self.width / 2, self.height / 2, self.width, self.height, WHITE))
        self.viewports.append(PerspectiveViewport(self.width / 2, 0, self.width, self.height / 2, BLACK, loc=[2.0, -3.0, 2.0], rot=[0.1, 0.0, 0.0]))
        self.viewports.append(PerspectiveViewport(0, 0, self.width / 2, self.height / 2, BLUE, loc=[0.0, 0.0, -4.0]))
        
        glShadeModel(GL_SMOOTH)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    
    def update(self, dt=None):
        glClear(GL_COLOR_BUFFER_BIT)
        
        for i, viewport in enumerate(self.viewports):
            viewport.render()
            #glClear(GL_DEPTH_BUFFER_BIT) # to here?
            #glMatrixMode (GL_MODELVIEW)
            #glLoadIdentity()
            #glClear (GL_DEPTH_BUFFER_BIT)
            
            # translate viewports here if needed + draw
            if 0:
                # old ortho draw (redundant). figure out right way to draw into ortho view
                glBegin(GL_QUADS)
                glTexCoord2f(1.0, 0.0); glVertex2i(self.width/2, 0)
                glTexCoord2f(0.0, 0.0); glVertex2i(0, 0)
                glTexCoord2f(0.0, 1.0); glVertex2i(0, self.height/2)
                glTexCoord2f(1.0, 1.0); glVertex2i(self.width/2, self.height/2)
                glEnd()
                self.label.draw() # not a good idea :P draws text inverted in depth direction. figure out nicer way. should probably restore view before drawing text
            glMatrixMode (GL_MODELVIEW)
            glLoadIdentity()
            glClear(GL_DEPTH_BUFFER_BIT) # needed?
            
            # generic draw (drawn for all viewports)
            glTranslatef(-1.5, 0.0, -6.0)
            glRotatef(self.rtri, 0.0, 1.0, 0.0)
            draw_pyramid()
            
            #glLoadIdentity() # without this makes cube orbit triangle (same space)
            glTranslatef(1.5, 0.0, -7.0)
            glRotatef(self.rquad, 1.0, 1.0, 1.0)
            draw_cube()
        
        if dt is None:
            dt = clock.tick()
        
        self.rtri += 40*dt
        self.rquad-= 40*dt
    
    def on_draw(self):
        self.update()
    
    def on_resize(self, width, height):
        # should rewrite this to work ok with viewport code!
        if height == 0:
            height=1
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1.0 * width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    _test()
    window = AppWindow()
    app.run()
