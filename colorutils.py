# -*- coding: utf-8 -*-
from random import random

from mathutils import clamp

RED = [1.0, 0.0, 0.0]
GREEN = [0.0, 1.0, 0.0]
BLUE = [0.0, 0.0, 1.0]
ORANGE = [1.0, 0.5, 0.0]
YELLOW = [1.0, 1.0, 0.0]
PURPLE = [1.0, 0.0, 1.0]
WHITE = [1.0, 1.0, 1.0]
BLACK = [0.0, 0.0, 0.0]

def get_color_instance(color):
    if isinstance(color, Color):
        return color
    elif type(color) is list:
        return Color(color)
    return Color()

def generate_random_color(variance=128, offset=128):
    color = []
    
    for col in range(3):
        val = int(random() * variance + offset)
        color.append(clamp(val, 0, 255))
    
    return color

class Color(): # convert to base class later if other color spaces are needed
    '''
    A color containing three color channels. They are considered red, green and blue by default.
    '''
    def __init__(self, rgb=[0.0, 0.0, 0.0]):
        '''
        pre:
            isinstance(rgb, list)
            rgb[0] >= 0.0
            rgb[1] >= 0.0
            rgb[2] >= 0.0
        '''
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]
    
    def __str__(self):
        '''
        
        >>> color = Color()
        >>> print color
        0.000 0.000 0.000
        >>> color = Color([0.5, 0.5, 1.0])
        >>> print color
        0.500 0.500 1.000
        '''
        return '%.3f %.3f %.3f' % (self.r, self.g, self.b)
    
    def __mul__(self, fac):
        '''
        
        >>> color1 = Color([0.5, 0.5, 1.0])
        >>> color2 = color1 * 2.0
        >>> print color2
        1.000 1.000 2.000
        '''
        if type(fac) is float:
            return Color([self.r * fac, self.g * fac, self.b * fac])
        raise NotImplementedError
    
    def quantize(self, fac=255):
        '''
        
        >>> color = Color([1.0, 1.0, 2.0])
        >>> color.quantize()
        [255.0, 255.0, 510.0]
        '''
        return [self.r * fac, self.g * fac, self.b * fac]
    
    def as_list(self):
        '''
        
        >>> color = Color([1.0, 0.5, 1.0])
        >>> color.as_list()
        [1.0, 0.5, 1.0]
        '''
        return [self.r, self.g, self.b]

# enable contract checking
import contract
contract.checkmod(__name__)

def _test():
    import doctest
    return doctest.testmod()

if __name__ == '__main__':
    _test()
