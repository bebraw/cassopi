# -*- coding: utf-8 -*-
from cassopi.utils.math.vector import Vector

def test_create_vector():
    vector = Vector()
    
    assert vector.dir.x == 0
    assert vector.dir.y == 0
    assert vector.dir.z == 0
    
    # add, subtract, mul, div, dot, length, normalize

def test_create_vector_with_values():
    vector = Vector(x=5.0, y=-2.0, z=4.0)
    
    #assert vector.
