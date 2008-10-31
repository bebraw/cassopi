# -*- coding: utf-8 -*-
#from cassopi.utils.math.vector import Vector

coordinates = ('x', 'y', 'z', )

# move elsewhere and finish and reuse! ...
class NamedArgsObject(object):
    def __init__(self, possible_args, **kwargs):
        for possible_arg in coordinates:
            self.__dict__[possible_arg] = check_arg(kwargs, possible_arg)

def check_arg(dict, arg):
    return dict[arg] if dict.has_key(arg) else 0

class Coordinate():
    def __init__(self, **kwargs):
        for coordinate in coordinates:
            self.__dict__[coordinate] = check_arg(kwargs, coordinate)
    
    def __str__(self):
        return '%.3f %.3f %.3f' % (self.x, self.y, self.z)
    
    def __add__(self, fac):
        if type(fac) in (float, int):
            return Coordinate(x=self.x + fac, y=self.y + fac, z=self.z + fac)
        
    def __div__(self, fac):
        if type(fac) in (float, int):
            return Coordinate(x=self.x / fac, y=self.y / fac, z=self.z / fac)
    
    def __mul__(self, fac):
        if isinstance(fac, Coordinate):
            return Coordinate(x=self.x * fac.x, y=self.y * fac.y, z=self.z * fac.z)
        #elif isinstance(fac, Vector):
        #    return self * fac.dir
        elif type(fac) in (float, int):
            return Coordinate(x=self.x * fac, y=self.y * fac, z=self.z * fac)
    
    def __sub__(self, fac):
        if isinstance(fac, Coordinate):
            return Coordinate(x=self.x - fac.x, y=self.y - fac.y, z=self.z - fac.z)
        #elif isinstance(fac, Vector):
        #    return self - fac.dir
        elif type(fac) in (float, int):
            return Coordinate(x=self.x - fac, y=self.y - fac, z=self.z - fac)
    
    def dot(self, fac):
        if isinstance(fac, Coordinate):
            n = self * fac
            return sum(n.__dict__.itervalues())
