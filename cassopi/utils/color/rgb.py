# -*- coding: utf-8 -*-

def get_rgb_color_instance(color):
    if isinstance(color, RGBColor):
        return color
    elif type(color) is list:
        return RGBColor(color)
    return RGBColor()

class RGBColor():
    '''
    A color containing red, green and blue color channels.
    They are defined as floats on range [0.0, 1.0].
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
        
        >>> color = RGBColor()
        >>> print color
        0.000 0.000 0.000
        >>> color = RGBColor([0.5, 0.5, 1.0])
        >>> print color
        0.500 0.500 1.000
        '''
        return '%.3f %.3f %.3f' % (self.r, self.g, self.b)
    
    def __mul__(self, fac):
        '''
        
        >>> color1 = RGBColor([0.5, 0.5, 1.0])
        >>> color2 = color1 * 2.0
        >>> print color2
        1.000 1.000 2.000
        '''
        if type(fac) is float:
            return Color([self.r * fac, self.g * fac, self.b * fac])
        raise NotImplementedError
    
    def quantize(self, fac=255):
        '''
        
        >>> color = RGBColor([1.0, 1.0, 2.0])
        >>> color.quantize()
        [255.0, 255.0, 510.0]
        '''
        return [self.r * fac, self.g * fac, self.b * fac]
    
    def as_list(self):
        '''
        
        >>> color = RGBColor([1.0, 0.5, 1.0])
        >>> color.as_list()
        [1.0, 0.5, 1.0]
        '''
        return [self.r, self.g, self.b]
