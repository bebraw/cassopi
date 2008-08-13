# -*- coding: utf-8 -*-
from math import acos, cos, hypot, pi, sqrt

ORIGIN = [0.0, 0.0, 0.0] # to constants?

def clamp(n, min_val, max_val):
    '''
    >>> a = 1.0; b = 2.0; c = 3.0
    >>> clamp(a, b, c)
    2.0
    >>> clamp(c, a, b)
    2.0
    >>> clamp(b, a, c)
    2.0
    '''
    n = max(n, min_val)
    n = min(n, max_val)
    return n

def mix(fac, n, m):
    '''
    >>> a = 0.0
    >>> b = 1.0
    >>> fac = 0.0
    >>> mix(fac, a, b)
    1.0
    >>> fac = 0.5
    >>> mix(fac, a, b)
    0.5
    >>> a = [0.0, 1.0, 0.5]
    >>> b = [1.0, 0.0, 0.5]
    >>> fac = 0.0
    >>> mix(fac, a, b)
    [1.0, 0.0, 0.5]
    >>> a = 1
    >>> b = 100
    >>> fac = 0.0
    >>> mix(fac, a, b)
    100
    '''
    if type(n) is float and type(m) is float:
        return n * fac + m * (1 - fac)
    if type(n) is int and type(m) is int:
        return int(n * fac + m * (1 - fac))
    if type(n) is list and type(m) is list:
        min_len = min(len(n), len(m))
        ret = []
        
        for i in range(min_len):
            ret.append(mix(fac, n[i], m[i]))
        
        return ret
    
    raise NotImplementedError

class XYZValue():
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
        >>> xyz = XYZValue()
        >>> print xyz
        0.000 0.000 0.000
        >>> xyz = XYZValue([1.0, 0.5, 0.0])
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
        >>> xyz = XYZValue([1.0, 3.0, 1.0])
        >>> print xyz.as_list()
        [1.0, 3.0, 1.0]
        '''
        return [self.x, self.y, self.z]
    
    def __add__(self, fac):
        '''
        >>> xyz = XYZValue()
        >>> sum_xyz = xyz + 5.0
        >>> print sum_xyz
        5.000 5.000 5.000
        >>> sum_xyz = xyz + 5
        >>> print sum_xyz
        5.000 5.000 5.000
        '''
        if type(fac) in (float, int):
            return XYZValue([self.x + fac, self.y + fac, self.z + fac])
        raise NotImplementedError
        
    def __div__(self, fac):
        '''
        >>> xyz = XYZValue([1.0, 1.0, 4.0])
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
            return XYZValue([self.x / fac, self.y / fac, self.z / fac])
        raise NotImplementedError
    
    def __mul__(self, fac):
        '''
        >>> xyz1 = XYZValue([1.0, 1.0, 4.0])
        >>> xyz2 = XYZValue([2.0, 2.0, 3.0])
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
        if isinstance(fac, XYZValue):
            return XYZValue([self.x * fac.x, self.y * fac.y, self.z * fac.z])
        elif isinstance(fac, Vector):
            return self * fac.dir
        elif type(fac) in (float, int):
            return XYZValue([self.x * fac, self.y * fac, self.z * fac])
        raise NotImplementedError
    
    def __sub__(self, fac):
        '''
        >>> xyz1 = XYZValue([1.0, 1.0, 4.0])
        >>> xyz2 = XYZValue([2.0, 2.0, 3.0])
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
        if isinstance(fac, XYZValue):
            return XYZValue([self.x - fac.x, self.y - fac.y, self.z - fac.z])
        elif isinstance(fac, Vector):
            return self - fac.dir
        elif type(fac) in (float, int):
            return XYZValue([self.x - fac, self.y - fac, self.z - fac])
        raise NotImplementedError
    
    def dot(self, fac):
        '''
        Remember that dot product results in scalar output! So this is not the same as * .
        
        >>> xyz1 = XYZValue([1.0, 3.0, 1.0])
        >>> xyz2 = XYZValue([2.0, 4.0, 2.0])
        >>> print xyz1.dot(xyz2)
        16.0
        '''
        if isinstance(fac, XYZValue):
            n = self * fac
            return sum(n.as_list())
        raise NotImplementedError

def get_coordinate_instance(coords):
    if isinstance(coords, Coordinate):
        return coords
    elif type(coords) is list:
        return Coordinate(coords)
    return Coordinate()

class Coordinate(XYZValue):
    '''
    Coordinate containing X, Y and Z elements. redundant?
    '''
    pass

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

class Space():
    '''
    X, Y, Z space. needed even? replace with matrix?
    '''
    def __init__(self, loc=[0.0, 0.0, 0.0], rot=[0.0, 0.0, 0.0]):
        '''
        pre:
            isinstance(loc, list)
            isinstance(rot, list)
            len(loc) == 3
            len(rot) == 3
        '''
        pass
        # validate the formulas!!!
        #self.x = Vector(acos(rot.y) / cos(rot.z)).normalize()
        #self.y = Vector(acos(rot.x) / cos(rot.z)).normalize()
        #self.z = Vector(acos(rot.x) / cos(rot.y)).normalize()

    def __str__(self):
        '''
        
        >>> space = Space()
        >>> print space
        foo
        '''
        return 'foo'
        #return '%.1f %.1f %.1f' % (self.x, self.y, self.z)

def get_rotation_instance(rot):
    if isinstance(rot, Rotation):
        return rot
    elif type(rot) is list:
        return Rotation(rot)
    return Rotation()

class Rotation(XYZValue):
    '''
    Rotation. 1.0 is full cycle.
    
    full = +-1.0 (use val % 1.0 to get abs. rot)
    '''
    def _to_n(self, n):
        return [self.x * n, self.y * n, self.z * n]
    
    def to_degrees(self):
        return self._to_n(360.0)
    
    def to_radians(self):
        return self._to_n(2 * pi)

class Normal():
    def __init__(self, vec1, vec2):
        pass

class Ray():
    ''' Ray has an origin and direction. These are defined using a pair of coordinates. Ray is
    considered to continue indefinitely.
    '''
    def __init__(self, origin=[0.0, 0.0, 0.0], dir=[1.0, 0.0, 0.0]):
        '''
        pre:
            isinstance(origin, list)
            isinstance(dir, list)
            len(origin) == 3
            len(dir) == 3
            origin != dir
        '''
        self.origin = Vector(origin)
        self.dir = Vector(dir)
    
    def __str__(self):
        '''
        >>> ray = Ray()
        >>> print ray
        origin: 0.000 0.000 0.000 direction: 1.000 0.000 0.000
        >>> ray = Ray([1.0, 1.0, 2.0], [-1.0, -2.0, 0.0])
        >>> print ray
        origin: 1.000 1.000 2.000 direction: -1.000 -2.000 0.000
        '''
        return 'origin: ' + str(self.origin) + ' direction: ' + str(self.dir)

def distance(a, b):
    '''
    Returns distance only if a and b are valid.
    
    >>> a = [0.0, 0.0]
    >>> b = [0.0, 0.0]
    >>> distance(a, b)
    0.0
    >>> a = [0.0, 0.0]
    >>> b = [1.0, 0.0]
    >>> distance(a, b)
    1.0
    >>> a = [0.0, 0.0]
    >>> b = [3.0, 4.0]
    >>> distance(a, b)
    5.0
    >>> a = [3.0, 4.0, 0.0]
    >>> distance(a, ORIGIN)
    5.0

    pre:
        isinstance(a, list)
        isinstance(b, list)
        len(a) > 0
        len(b) > 0
    '''
    def distance_recursion(a, b, dist, step):
        if step < len(a) - 1 and step < len(b) - 1:
            dist += hypot(dist, a[step] - b[step])
            return distance_recursion(a, b, dist, step + 1)
        
        return dist
    return distance_recursion(a, b, hypot(a[0] - b[0], a[1] - b[1]), 2)

# enable contract checking
import contract
contract.checkmod(__name__)

def _test():
    import doctest
    return doctest.testmod()

if __name__ == '__main__':
    _test()
