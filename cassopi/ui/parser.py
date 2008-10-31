from paddings import Padding
from containers import VerticalContainer
from cassopi.utils.yaml.parser import read_yaml

def parse_ui(structure):
    content = read_yaml(structure)
    root = content['vertical_container']
    return parse_vertical_container(root)

def parse_vertical_container(content):
    padding = None
    
    if content:
        padding = Padding(**content['padding'])
    
    return VerticalContainer(padding=padding)
