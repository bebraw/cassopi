directions = ('top', 'bottom', 'left', 'right', )

def check_arg(dict, arg):
    return max(dict[arg] if dict.has_key(arg) else 0, 0)

class Padding():
    def __init__(self, **kwargs):
        if kwargs.has_key('all'):
            for direction in directions:
                kwargs[direction] = kwargs['all']
        
        for direction in directions:
            self.__dict__[direction] = check_arg(kwargs, direction)
