# -*- coding: utf-8 -*-
"""
Vector (3d) class.
"""

from coordinate import Coordinate

class Vector():
    '''
    Vector containing X, Y and Z components. Vector is always relative to origin.
    '''
    def __init__(self, dir=[0.0, 0.0, 0.0]):
        '''
        pre:
            isinstance(dir, list)
            len(dir) == 3
        '''
        self.dir = Coordinate(dir)
    
    def __str__(self):
        '''
        >>> vector = Vector()
        >>> print vector
        0.000 0.000 0.000
        >>> vector = Vector([1.0, 1.0, 1.0])
        >>> print vector
        1.000 1.000 1.000
        '''
        return str(self.dir)
    
    def __sub__(self, fac):
        '''
        >>> vector1 = Vector([1.0, 2.0, 3.0])
        >>> vector2 = Vector([3.0, 2.0, 2.0])
        >>> sub_vector = vector1 - vector2
        >>> print sub_vector
        -2.000 0.000 1.000
        >>> coord = Coordinate([2.0, 1.0, 3.0])
        >>> sub_vector_coord = vector1 - coord
        >>> print sub_vector_coord
        -1.000 1.000 0.000
        >>> sub_vector_float = vector1 - 2.0
        >>> print sub_vector_float
        -1.000 0.000 1.000
        >>> sub_vector_int = vector1 - 2
        >>> print sub_vector_int
        -1.000 0.000 1.000
        '''
        if isinstance(fac, Vector):
            sub = self.dir - fac.dir
            return Vector(sub.as_list())
        elif isinstance(fac, Coordinate):
            sub = self.dir - fac
            return Vector(sub.as_list())
        elif type(fac) in (float, int):
            sub = self.dir - fac
            return Vector(sub.as_list())
        raise NotImplementedError
    
    def __mul__(self, fac):
        '''
        >>> vector1 = Vector([1.0, 2.0, 3.0])
        >>> vector2 = Vector([3.0, -1.0, 5.0])
        >>> vector_mul = vector1 * vector2
        >>> print vector_mul
        3.000 -2.000 15.000
        >>> vector_float_mul = vector1 * 2.0
        >>> print vector_float_mul
        2.000 4.000 6.000
        >>> vector_int_mul = vector1 * 2
        >>> print vector_int_mul
        2.000 4.000 6.000
        '''
        if isinstance(fac, Vector): # cross product
            mul = self.dir * fac.dir
            return Vector(mul.as_list())
        elif type(fac) in (float, int):
            mul = self.dir * fac
            return Vector(mul.as_list())
        raise NotImplementedError
    
    def dot(self, fac):
        ''' Also known as scalar product due to output.
        
        >>> vector1 = Vector([1.0, 2.0, 3.0])
        >>> vector2 = Vector([4.0, 1.0, 2.0])
        >>> vector1.dot(vector2)
        12.0
        >>> coord = Coordinate([1.0, 2.0, -1.0])
        >>> vector1.dot(coord)
        2.0
        '''
        if isinstance(fac, Vector):
            n = self.dir * fac.dir
            return sum(n.as_list())
        elif isinstance(fac, Coordinate):
            n = self.dir * fac
            return sum(n.as_list())
        raise NotImplementedError
    
    def length(self):
        '''
        >>> vector = Vector([3.0, 4.0, 0.0])
        >>> vector.length()
        5.0
        '''
        return distance(ORIGIN, self.dir.as_list())
    
    def normalize(self):
        '''
        >>> vector = Vector([3.0, 4.0, 0.0])
        >>> vector.normalize()
        >>> vector.length()
        1.0
        >>> print vector
        0.600 0.800 0.000
        '''
        self.dir = self.dir / self.length()
