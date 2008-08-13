# -*- coding: utf-8 -*-
import ctypes
from math import cos, pi, sin

from pyglet import app, clock, window
from pyglet.gl import *

from colorutils import * # not a good dependency!
from mathutils import *
from tesselator import Tesselator

def draw_vertex(v, vcol):
    if vcol: glColor3f(*vcol)
    glVertex3f(*v)

def draw_triangle(a, b, c, acol, bcol=None, ccol=None):
    draw_vertex(a, acol)
    draw_vertex(b, bcol)
    draw_vertex(c, ccol)

def draw_quad(a, b, c, d, acol, bcol=None, ccol=None, dcol=None):
    draw_triangle(a, b, c, acol, bcol, ccol)
    draw_vertex(d, dcol)

class Triangle():
    def __init__(self, a, b, c, acol, bcol=None, ccol=None):
        self.a = a
        self.b = b
        self.c = c
        self.acol = acol
        self.bcol = bcol
        self.ccol = ccol
    
    def render(self):
        draw_triangle(self.a, self.b, self.c, self.acol, self.bcol, self.ccol)

class Quad():
    def __init__(self, a, b, c, d, acol, bcol=None, ccol=None, dcol=None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

class Vertex():
    def __init__(self, coords=None, color=None):
        self.coords = get_coordinate_instance(coords)
        self.color = get_color_instance(color)
    
    def __str__(self):
        '''
        >>> vertex = Vertex()
        >>> print vertex
        coords: 0.000 0.000 0.000 color: 0.000 0.000 0.000
        >>> vertex = Vertex(Coordinate())
        >>> print vertex
        coords: 0.000 0.000 0.000 color: 0.000 0.000 0.000
        >>> vertex = Vertex(Coordinate([0.5, 1.0, 1.0]))
        >>> print vertex
        coords: 0.500 1.000 1.000 color: 0.000 0.000 0.000
        >>> vertex = Vertex(Coordinate([0.5, 1.0, 1.0]), Color(ORANGE))
        >>> print vertex
        coords: 0.500 1.000 1.000 color: 1.000 0.500 0.000
        >>> vertex = Vertex([1.0, 0.5, 1.0])
        >>> print vertex
        coords: 1.000 0.500 1.000 color: 0.000 0.000 0.000
        >>> vertex = Vertex(color=[1.0, 0.5, 0.5])
        >>> print vertex
        coords: 0.000 0.000 0.000 color: 1.000 0.500 0.500
        '''
        return 'coords: ' + str(self.coords) + ' color: ' + str(self.color)

class Polygon():
    # make it easy to alter polygon data???
    def __init__(self, vertices=None):
        vertices_ok = False
        
        if type(vertices) is list:
            vertices_ok = True
            
            for vertex in vertices:
                if not isinstance(vertex, Vertex):
                    vertices_ok = False
                    break
        
        if vertices_ok:
            self.vertices = vertices
        else:
            self.vertices = []
        
        self.tesselator = Tesselator()
    
    def __str__(self):
        '''
        >>> polygon = Polygon()
        >>> print polygon
        no vertex data!
        >>> vertex1 = Vertex()
        >>> vertex2 = Vertex([0.5, 1.0, 0.5])
        >>> vertex3 = Vertex([-0.5, 1.0, 0.5])
        >>> vertex_list = [vertex1, vertex2, vertex3]
        >>> polygon = Polygon(vertex_list)
        >>> print polygon
        coords: 0.000 0.000 0.000 color: 0.000 0.000 0.000
        coords: 0.500 1.000 0.500 color: 0.000 0.000 0.000
        coords: -0.500 1.000 0.500 color: 0.000 0.000 0.000
        '''
        str_list = []
        
        for i, vertex in enumerate(self.vertices):
            str_list.append(str(vertex))
            
            # add newlines. a bit clunky but works
            if i < len(self.vertices) - 1:
                str_list.append('\n')
        
        ret = ''.join(str_list)
        
        if ret:
            return ret
        return 'no vertex data!'
    
    def render(self):
        self.tesselator.update_vertex_data(self.vertices) # should do this only if vertex data has changed
        self.tesselator.render()

def draw_circle(corners, top_center, bottom_y):
    # clean up!
    step = 2 * pi / corners
    val = 0.0
    
    for side in range(corners):
        coord1 = (cos(val), bottom_y, sin(val))
        val += step
        coord2 = (cos(val), bottom_y, sin(val))
        
        draw_triangle(top_center, coord1, coord2, RED, GREEN, GREEN)

def draw_pyramid(corners=4):
    top_center = (0.0, 1.0, 0.0)
    bottom_y = -1.0
    bottom_center = (0.0, bottom_y, 0.0)
    coord1 = coord2 = None
    
    glBegin(GL_TRIANGLES)
    draw_circle(corners, top_center, bottom_y)
    draw_circle(corners, bottom_center, bottom_y)
    glEnd()

def draw_cube():
    # could get coords using basic math? (2 circles (4 corners) -> coords. use these to get remaining 4 sides?
    a = (1.0, 1.0, -1.0)
    b = (-1.0, 1.0, -1.0)
    c = (-1.0, 1.0, 1.0)
    d = (1.0, 1.0, 1.0)
    e = (1.0, -1.0, 1.0)
    f = (-1.0, -1.0, 1.0)
    g = (-1.0, -1.0, -1.0)
    h = (1.0, -1.0, -1.0)
    
    glBegin(GL_QUADS)
    draw_quad(a, b, c, d, GREEN)
    draw_quad(e, f, g, h, ORANGE)
    draw_quad(d, c, f, e, RED)
    draw_quad(h, g, b, a, YELLOW)
    draw_quad(c, b, g, f, BLUE)
    draw_quad(a, d, e, h, PURPLE)
    glEnd()

class TestWindow(window.Window):
    def __init__(self, width=640, height=480, resizable=True, visible=True):
        super(TestWindow, self).__init__(width=width, height=height, resizable=resizable, visible=visible)
        
        self.rpoly = 0.0
        clock.schedule_interval(self.update, 0.01)
        
        vertex1 = Vertex([0.0, 1.0, 0.0], color=RED)
        vertex2 = Vertex([-1.0, -1.0, 1.0], color=GREEN)
        vertex3 = Vertex([1.0, -1.0, 1.0], color=BLUE)
        vertex4 = Vertex([1.0, -1.0, -1.0], color=GREEN)
        vertex5 = Vertex([0.0, -3.0, -3.0], color=GREEN)
        
        a = Vertex([1.0, 1.0, -1.0], color=RED)
        b = Vertex([-1.0, 1.0, -1.0], color=GREEN)
        c = Vertex([-1.0, 1.0, -2.0], color=ORANGE)
        d = Vertex([-2.0, 1.0, 1.0], color=BLUE)
        e = Vertex([1.0, 1.0, 1.0], color=RED)
        
        vertex_list1 = [vertex1, vertex2, vertex3]
        vertex_list2 = [vertex1, vertex3, vertex4]
        vertex_list3 = [a, b, c, d, e]
        self.polygon1 = Polygon(vertex_list1)
        self.polygon2 = Polygon(vertex_list2)
        self.polygon3 = Polygon(vertex_list3)
        
        glShadeModel(GL_SMOOTH)
        glClearColor(1.0, 1.0, 1.0, 0.0) # bg color
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    
    def update(self, dt=None):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        glTranslatef(-1.5, 0.0, -6.0)
        
        glRotatef(self.rpoly, 0.0, 1.0, 0.0)
        
        self.polygon1.render()
        self.polygon2.render()
        self.polygon3.render()
        
        #draw_cube()
        
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
