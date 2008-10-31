# -*- coding: utf-8 -*-
from cassopi.ui.containers import HorizontalContainer, VerticalContainer
from cassopi.ui.parser import StructureParser
from cassopi.utils.yaml.parser import read_yaml

minimal_structure = '''
VerticalContainer:
'''

def test_StructureParser_parse_minimal():
    structure_parser = StructureParser(minimal_structure)
    
    assert isinstance(structure_parser, StructureParser)
    root = structure_parser.parse()
    assert isinstance(root, VerticalContainer)

structure_with_padding_in_all_directions = '''
VerticalContainer:
    padding:
        top: 5
        left: 10
        right: 15
        bottom: 20
'''

def test_StructureParser_parse_vertical_container_with_padding():
    structure_parser = StructureParser(structure_with_padding_in_all_directions)
    
    root = structure_parser.parse()
    assert isinstance(root, VerticalContainer)
    assert root.padding.top == 5
    assert root.padding.left == 10
    assert root.padding.right == 15
    assert root.padding.bottom == 20

structure_with_all_padding = '''
VerticalContainer:
    padding:
        all: 10
'''

def test_StructureParser_parse_container_with_all_padding():
    structure_parser = StructureParser(structure_with_all_padding)
    
    root = structure_parser.parse()
    assert isinstance(root, VerticalContainer)
    assert root.padding.top == 10
    assert root.padding.left == 10
    assert root.padding.right == 10
    assert root.padding.bottom == 10

structure_with_another_vertical_container = '''
VerticalContainer:
    padding:
        all: 10
    children:
        - VerticalContainer:
            padding:
                right: 15
                left: 5
'''

def test_StructureParser_parse_hierarchy_with_children():
    structure_parser = StructureParser(structure_with_another_vertical_container)
    
    root = structure_parser.parse()
    assert isinstance(root, VerticalContainer)
    assert root.padding.top == 10
    assert root.padding.left == 10
    assert root.padding.right == 10
    assert root.padding.bottom == 10
    
    root_child = root.children[0]
    
    assert isinstance(root_child, VerticalContainer)
    assert root_child.padding.top == 0
    assert root_child.padding.left == 5
    assert root_child.padding.right == 15
    assert root_child.padding.bottom == 0

structure_with_another_horizontal_container = '''
VerticalContainer:
    padding:
        all: 10
    children:
        - HorizontalContainer:
            padding:
                right: 5
                top: 50
'''

def test_StructureParser_parse_hierarchy_with_children_and_horizontal_container():
    structure_parser = StructureParser(structure_with_another_horizontal_container)
    
    root = structure_parser.parse()
    assert isinstance(root, VerticalContainer)
    assert root.padding.top == 10
    assert root.padding.left == 10
    assert root.padding.right == 10
    assert root.padding.bottom == 10
    
    root_child = root.children[0]
    
    assert isinstance(root_child, HorizontalContainer)
    assert root_child.padding.top == 50
    assert root_child.padding.left == 0
    assert root_child.padding.right == 5
    assert root_child.padding.bottom == 0

structure_with_multiple_containers = '''
VerticalContainer:
    padding:
        all: 10
    children:
        - HorizontalContainer:
            padding:
                right: 25
                top: 5
        - VerticalContainer:
            padding:
                left: 20
                right: 5
'''

def test_StructureParser_parse_hierarchy_with_multiple_containers():
    structure_parser = StructureParser(structure_with_multiple_containers)
    
    root = structure_parser.parse()
    assert isinstance(root, VerticalContainer)
    assert root.padding.top == 10
    assert root.padding.left == 10
    assert root.padding.right == 10
    assert root.padding.bottom == 10
    
    root_child = root.children[0]
    
    assert isinstance(root_child, HorizontalContainer)
    assert root_child.padding.top == 5
    assert root_child.padding.left == 0
    assert root_child.padding.right == 25
    assert root_child.padding.bottom == 0
    
    root_child2 = root.children[1]
    
    assert isinstance(root_child2, VerticalContainer)
    assert root_child2.padding.top == 0
    assert root_child2.padding.left == 20
    assert root_child2.padding.right == 5
    assert root_child2.padding.bottom == 0
