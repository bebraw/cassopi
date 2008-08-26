# -*- coding: utf-8 -*-
"""
Rotation (3d) class.
"""

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
