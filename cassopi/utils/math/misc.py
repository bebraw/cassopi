# -*- coding: utf-8 -*-
"""
Miscellaneous math functions.
"""

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
