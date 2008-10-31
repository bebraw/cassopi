from yaml import load

def read_yaml(document):
    try:
        file_stream = file(document, 'r')
    except IOError:
        file_stream = document
    
    structure = load(file_stream)
    
    return structure if structure != document else None
