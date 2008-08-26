# -*- coding: utf-8 -*-
"""
Ray (3d) class.
"""

from vector import Vector

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
