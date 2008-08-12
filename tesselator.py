# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *

class RenderVertex():
    def __init__(self, vertex):
        vertex_data_as_list = vertex.coords.as_list() + vertex.color.as_list() # add rest as needed
        self.data = (ctypes.c_double * len(vertex_data_as_list))(*vertex_data_as_list)

class Tesselator():
    def __init__(self, vertices=None, winding=GLU_TESS_WINDING_ODD, force_triangles = True):
        self.tess = gluNewTess()
        gluTessCallback(self.tess, GLU_TESS_BEGIN, glBegin)
        gluTessCallback(self.tess, GLU_TESS_VERTEX, self.vertex)
        gluTessCallback(self.tess, GLU_TESS_COMBINE, self.combine)
        gluTessCallback(self.tess, GLU_TESS_END, glEnd)
        gluTessProperty(self.tess, GLU_TESS_WINDING_RULE, winding)
        
        self.current = []
        self.result = []
        self.force_triangles = force_triangles
    
    def __del__(self):
        gluDeleteTess(self.tess)
    
    def update_vertex_data(self, vertices):
        self.render_vertices = []
        for vertex in vertices:
            self.render_vertices.append(RenderVertex(vertex))
    
    def render(self):
        gluTessBeginPolygon(self.tess, None)
        gluTessBeginContour(self.tess)
        
        for render_vertex in self.render_vertices:
            gluTessVertex(self.tess, render_vertex.data[:3], render_vertex.data)
        
        gluTessEndContour(self.tess)
        gluTessEndPolygon(self.tess)
    
    # tesselator callbacks
    def vertex(self, vertex):
        glVertex3dv(vertex[:3]);
        glColor3dv(vertex[3:6]);
    
    def combine(self, new_position, vertices, weights):
        u, v = 0, 0
        
        for vertex, weight in map(None, vertices, weights):
            if vertex:
                u += vertex.texCoord[0] * weight
                v += vertex.texCoord[1] * weight
        
        return self.dataClass(new_position, (u, v))
