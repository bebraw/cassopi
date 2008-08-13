#!/usr/bin/env python
"""
Tests contracts and available contracts from given file. Contract
checks are not executed if required module is not found. Name of the
module to be tested is passed as the first parameter to the script.
"""
def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


if __name__ == '__main__':
    from sys import argv
    
    print 'Running tests.'
    
    print 'Importing given module'
    try:
        module = my_import(argv[1])
    except Exception, e:
        print 'Error while trying to import given module.'
        print e
        quit()
    
    print 'Checking contracts'
    try:
        import contract
        contract.checkmod(module)
    except Exception, e:
        print 'Error while trying to check contracts!'
        print e
    
    print 'Checking doctests'
    import doctest
    doctest.testmod(module)
    
    # add coverage test here
    
    # unit tests?
    
    print 'Tests finished.'
