from paddings import Padding
from containers import HorizontalContainer, VerticalContainer
from cassopi.utils.yaml.parser import read_yaml

def parse_ui(structure):
    content = read_yaml(structure)
    root = content['vertical_container']
    result = parse_vertical_container(root)
    
    if root and root.has_key('contains'):
        for node in root['contains']:
            if node.has_key('vertical_container'):
                node = node['vertical_container']
                vertical_container = parse_vertical_container(node)
                result.children.append(vertical_container)
            
            if node.has_key('horizontal_container'):
                node = node['horizontal_container']
                horizontal_container = parse_horizontal_container(node)
                result.children.append(horizontal_container)
    
    return result

def parse_horizontal_container(content):
    padding = None
    
    if content:
        padding = Padding(**content['padding'])
    
    return HorizontalContainer(padding=padding)

def parse_vertical_container(content):
    padding = None
    
    if content:
        padding = Padding(**content['padding'])
    
    return VerticalContainer(padding=padding)
