# -*- coding: utf-8 -*-
from pyglet import app, clock, window
from pyglet.gl import *
from pyglet.window import key

from colorutils import *
from drawutils import Polygon, Vertex
from mathutils import *

class Viewport(object):
    def __init__(self, bottom_x, bottom_y, top_x, top_y, bg_color):
        self.x = int(bottom_x)
        self.y = int(bottom_y)
        self.width = int(max(top_x - bottom_x, 1.0))
        self.height = int(max(top_y - bottom_y, 1.0))
        self.bg_color = get_color_instance(bg_color)
    
    def render(self):
        r, g, b = self.bg_color.as_list()
        glClearColor(r, g, b, 0.0)
        
        glScissor(self.x, self.y, self.width, self.height)
        glEnable(GL_SCISSOR_TEST)
        
        glClear(GL_COLOR_BUFFER_BIT) # should clear depth buffer also?
        glViewport(self.x, self.y, self.width, self.height)
        
        glDisable(GL_SCISSOR_TEST)
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

class PerspectiveViewport(Viewport):
    def __init__(self, bottom_x, bottom_y, top_x, top_y, bg_color, loc=None, rot=None, fov_y=45.0, clip_near=0.1, clip_far=500.0):
        super(PerspectiveViewport, self).__init__(bottom_x, bottom_y, top_x, top_y, bg_color)
        self.loc = get_coordinate_instance(loc)
        self.rot = get_rotation_instance(rot)
        self.fov_y = fov_y
        self.clip_near = clip_near
        self.clip_far = clip_far
    
    def render(self):
        super(PerspectiveViewport, self).render()
        gluPerspective(self.fov_y, self.width / self.height, self.clip_near, self.clip_far)
        
        x_rot, y_rot, z_rot = self.rot.to_degrees()
        glRotatef(x_rot, 1.0, 0.0, 0.0)
        glRotatef(y_rot, 0.0, 1.0, 0.0)
        glRotatef(z_rot, 0.0, 0.0, 1.0)
        
        glTranslatef(*self.loc.as_list())

class OrthoViewport(Viewport):
    def __init__(self, bottom_x, bottom_y, top_x, top_y, bg_color):
        super(OrthoViewport, self).__init__(bottom_x, bottom_y, top_x, top_y, bg_color)
    
    def render(self):
        super(OrthoViewport, self).render()
        gluOrtho2D(self.x, self.width / 2, self.height / 2, self.y) # validate this!
        #glMatrixMode(GL_PROJECTION);
        #glLoadIdentity();
        #glOrtho(-1, 1, -1, 1, -1.0, 1.0);

class TestWindow(window.Window):
    def __init__(self, width=640, height=480, resizable=True, visible=True):
        super(TestWindow, self).__init__(width=width, height=height, resizable=resizable, visible=visible)
        
        self.viewport = PerspectiveViewport(0, 0, self.width, self.height, YELLOW, [1.0, 0.5, -5.0], [0.0, 0.0, 0.0])
        self.rpoly = 0.0
        self.pressed_key = None
        
        clock.schedule_interval(self.update, 0.01)
        clock.schedule_interval(self.update_pressed_key, 0.1)
        
        a = Vertex([1.0, 1.0, -1.0], color=RED)
        b = Vertex([-1.0, 1.0, -1.0], color=GREEN)
        c = Vertex([-1.0, 1.0, -2.0], color=ORANGE)
        d = Vertex([-2.0, 1.0, 1.0], color=BLUE)
        e = Vertex([1.0, 1.0, 1.0], color=RED)
        
        vertex_list = [a, b, c, d, e]
        self.polygon = Polygon(vertex_list)
        
        glShadeModel(GL_SMOOTH)
        glClearColor(1.0, 1.0, 1.0, 0.0) # bg color
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    
    def update(self, dt=None):
        glClear(GL_COLOR_BUFFER_BIT)
        
        self.viewport.render()
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_DEPTH_BUFFER_BIT)
        
        glLoadIdentity()
        glTranslatef(-1.5, 0.0, -6.0)
        #glRotatef(self.rpoly, 0.0, 1.0, 0.0)
        
        self.polygon.render()
        
        if dt is None:
            dt = clock.tick()
        
        self.rpoly += 40*dt
    
    def on_draw(self):
        self.update()
    
    def on_resize(self, width, height):
        if height == 0:
            height=1
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1.0 * width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    
    def update_pressed_key(self, dt=None):
        loc_offset = 1.1
        rot_offset = 0.01
        
        try:
            operator, offset = {
                key.A: (self.viewport.rot.offset_x, -rot_offset),
                key.S: (self.viewport.rot.offset_x, rot_offset),
                key.Q: (self.viewport.rot.offset_y, -rot_offset),
                key.W: (self.viewport.rot.offset_y, rot_offset),
                key.Z: (self.viewport.rot.offset_z, -rot_offset),
                key.X: (self.viewport.rot.offset_z, rot_offset),
                key.UP: (self.viewport.loc.offset_z, loc_offset),
                key.DOWN: (self.viewport.loc.offset_z, -loc_offset),
                key.LEFT: (self.viewport.loc.offset_x, loc_offset),
                key.RIGHT: (self.viewport.loc.offset_x, -loc_offset),
            }[self.pressed_key]
            
            operator(offset=offset)
        except KeyError:
            pass
    
    def on_key_press(self, symbol, modifiers):
        self.pressed_key = symbol
    
    def on_key_release(self, symbol, modifiers):
        self.pressed_key = None

# enable contract checking
import contract
contract.checkmod(__name__)

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    _test()
    window1 = TestWindow()
    app.run()
