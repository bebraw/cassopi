# -*- coding: utf-8 -*-
from cassopi.utils.math.coordinate import Coordinate
from cassopi.utils.math.vector import Vector

def test_create_empty_coordinate():
    coordinate = Coordinate()
    
    assert coordinate.x == 0
    assert coordinate.y == 0
    assert coordinate.z == 0

def test_create_coordinate_with_values():
    coordinate = Coordinate(x=5.0, y=3.0, z=7.0)
    
    assert coordinate.x == 5.0
    assert coordinate.y == 3.0
    assert coordinate.z == 7.0

def test_coordinate_as_string():
    coordinate = Coordinate(x=5.0, y=3.0, z=7.0)
    
    assert str(coordinate) == '5.000 3.000 7.000'

def test_coordinate_add():
    coordinate = Coordinate(x=5.0, y=3.0, z=7.0)
    
    coordinate_sum = coordinate + 5
    
    assert coordinate_sum.x == 10.0
    assert coordinate_sum.y == 8.0
    assert coordinate_sum.z == 12.0
    
    coordinate_sum = coordinate + 5.0
    
    assert coordinate_sum.x == 10.0
    assert coordinate_sum.y == 8.0
    assert coordinate_sum.z == 12.0

def test_coordinate_div():
    coordinate = Coordinate(x=5.0, y=3.0, z=7.0)
    
    coordinate_div = coordinate / 2
    
    assert coordinate_div.x == 2.5
    assert coordinate_div.y == 1.5
    assert coordinate_div.z == 3.5
    
    coordinate_div = coordinate / 2.0
    
    assert coordinate_div.x == 2.5
    assert coordinate_div.y == 1.5
    assert coordinate_div.z == 3.5

def test_coordinate_mul():
    coordinate1 = Coordinate(x=5.0, y=3.0, z=7.0)
    coordinate2 = Coordinate(x=3.0, y=-2.0, z=4.0)
    
    coordinate_mul = coordinate1 * coordinate2
    
    assert coordinate_mul.x == 15.0
    assert coordinate_mul.y == -6.0
    assert coordinate_mul.z == 28.0
    
    #vector = Vector(x=3.0, y=5.0, z=-1.0)
    
    #coordinate_mul = coordinate1 * vector
    
    #assert coordinate_mul.x == 15.0
    #assert coordinate_mul.y == 15.0
    #assert coordinate_mul.z == -7.0
    
    coordinate_mul = coordinate1 * 4.0
    
    assert coordinate_mul.x == 20.0
    assert coordinate_mul.y == 12.0
    assert coordinate_mul.z == 28.0
    
    coordinate_mul = coordinate1 * 4
    
    assert coordinate_mul.x == 20.0
    assert coordinate_mul.y == 12.0
    assert coordinate_mul.z == 28.0

def test_coordinate_sub():
    coordinate1 = Coordinate(x=5.0, y=3.0, z=7.0)
    coordinate2 = Coordinate(x=3.0, y=-2.0, z=4.0)
    
    coordinate_sub = coordinate1 - coordinate2
    
    assert coordinate_sub.x == 2.0
    assert coordinate_sub.y == 5.0
    assert coordinate_sub.z == 3.0
    
    #vector = Vector(x=3.0, y=5.0, z=-1.0)
    
    #coordinate_sub = coordinate1 - vector
    
    #assert coordinate_sub.x == 2.0
    #assert coordinate_sub.y == -2.0
    #assert coordinate_sub.z == 6.0
    
    coordinate_sub = coordinate1 - 4.0
    
    assert coordinate_sub.x == 1.0
    assert coordinate_sub.y == -1.0
    assert coordinate_sub.z == 3.0
    
    coordinate_sub = coordinate1 - 4
    
    assert coordinate_sub.x == 1.0
    assert coordinate_sub.y == -1.0
    assert coordinate_sub.z == 3.0

def test_dot_product():
    coordinate1 = Coordinate(x=1.0, y=3.0, z=1.0)
    coordinate2 = Coordinate(x=2.0, y=4.0, z=2.0)
    
    dot_product = coordinate1.dot(coordinate2)
    
    assert dot_product == 16.0
