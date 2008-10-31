from elements import AbstractElement

class Padding(AbstractElement):
    suitable_values = ('top', 'bottom', 'left', 'right', )
    
    def __init__(self, args=None):
        for suitable_value in self.suitable_values:
            self.__dict__[suitable_value] = 0
        
        if args and args.has_key('all'):
            for suitable_value in self.suitable_values:
                args[suitable_value] = args['all']
        
        super(Padding, self).__init__(args)
        
    def check_arg(self, dict, arg):
        return max(dict[arg] if dict.has_key(arg) else 0, 0)
