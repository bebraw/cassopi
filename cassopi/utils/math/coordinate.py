# -*- coding: utf-8 -*-
"""
Coordinate (3d) class.
"""

def get_coordinate_instance(coords):
    if isinstance(coords, Coordinate):
        return coords
    elif type(coords) is list:
        return Coordinate(coords)
    return Coordinate()

class Coordinate():
    def __init__(self, val=[0.0, 0.0, 0.0]):
        '''
        pre:
            isinstance(val, list)
            len(val) == 3
        '''
        self.x = val[0]
        self.y = val[1]
        self.z = val[2]
    
    def __str__(self):
        '''
        >>> xyz = Coordinate()
        >>> print xyz
        0.000 0.000 0.000
        >>> xyz = Coordinate([1.0, 0.5, 0.0])
        >>> print xyz
        1.000 0.500 0.000
        '''
        return '%.3f %.3f %.3f' % (self.x, self.y, self.z)
    
    def offset_x(self, offset):
        self.x += offset
    
    def offset_y(self, offset):
        self.y += offset
    
    def offset_z(self, offset):
        self.z += offset
    
    def as_list(self):
        '''
        >>> xyz = Coordinate([1.0, 3.0, 1.0])
        >>> print xyz.as_list()
        [1.0, 3.0, 1.0]
        '''
        return [self.x, self.y, self.z]
    
    def __add__(self, fac):
        '''
        >>> xyz = Coordinate()
        >>> sum_xyz = xyz + 5.0
        >>> print sum_xyz
        5.000 5.000 5.000
        >>> sum_xyz = xyz + 5
        >>> print sum_xyz
        5.000 5.000 5.000
        '''
        if type(fac) in (float, int):
            return Coordinate([self.x + fac, self.y + fac, self.z + fac])
        raise NotImplementedError
        
    def __div__(self, fac):
        '''
        >>> xyz = Coordinate([1.0, 1.0, 4.0])
        >>> div_xyz = xyz / 2.0
        >>> print div_xyz
        0.500 0.500 2.000
        >>> div_xyz = xyz / 2
        >>> print div_xyz
        0.500 0.500 2.000
        
        pre:
            fac != 0.0
            fac != 0
        '''
        if type(fac) in (float, int):
            return Coordinate([self.x / fac, self.y / fac, self.z / fac])
        raise NotImplementedError
    
    def __mul__(self, fac):
        '''
        >>> xyz1 = Coordinate([1.0, 1.0, 4.0])
        >>> xyz2 = Coordinate([2.0, 2.0, 3.0])
        >>> mul_xyz = xyz1 * xyz2
        >>> print mul_xyz
        2.000 2.000 12.000
        >>> vector = Vector([2.0, 3.0, 4.0])
        >>> mul_xyz = xyz1 * vector
        >>> print mul_xyz
        2.000 3.000 16.000
        >>> mul_xyz = xyz1 * 3.0
        >>> print mul_xyz
        3.000 3.000 12.000
        >>> mul_xyz = xyz1 * 3
        >>> print mul_xyz
        3.000 3.000 12.000
        
        pre:
            fac != 0.0
        '''
        if isinstance(fac, Coordinate):
            return Coordinate([self.x * fac.x, self.y * fac.y, self.z * fac.z])
        elif isinstance(fac, Vector):
            return self * fac.dir
        elif type(fac) in (float, int):
            return Coordinate([self.x * fac, self.y * fac, self.z * fac])
        raise NotImplementedError
    
    def __sub__(self, fac):
        '''
        >>> xyz1 = Coordinate([1.0, 1.0, 4.0])
        >>> xyz2 = Coordinate([2.0, 2.0, 3.0])
        >>> sub_xyz = xyz1 - xyz2
        >>> print sub_xyz
        -1.000 -1.000 1.000
        >>> vector = Vector([2.0, 3.0, 4.0])
        >>> sub_xyz = xyz1 - vector
        >>> print sub_xyz
        -1.000 -2.000 0.000
        >>> mul_xyz = xyz1 - 3.0
        >>> print mul_xyz
        -2.000 -2.000 1.000
        >>> mul_xyz = xyz1 - 3
        >>> print mul_xyz
        -2.000 -2.000 1.000
        '''
        if isinstance(fac, Coordinate):
            return Coordinate([self.x - fac.x, self.y - fac.y, self.z - fac.z])
        elif isinstance(fac, Vector):
            return self - fac.dir
        elif type(fac) in (float, int):
            return Coordinate([self.x - fac, self.y - fac, self.z - fac])
        raise NotImplementedError
    
    def dot(self, fac):
        '''
        Remember that dot product results in scalar output! So this is not the same as * .
        
        >>> xyz1 = Coordinate([1.0, 3.0, 1.0])
        >>> xyz2 = Coordinate([2.0, 4.0, 2.0])
        >>> print xyz1.dot(xyz2)
        16.0
        '''
        if isinstance(fac, Coordinate):
            n = self * fac
            return sum(n.as_list())
        raise NotImplementedError
