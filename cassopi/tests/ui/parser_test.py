# -*- coding: utf-8 -*-
from cassopi.ui.containers import HorizontalContainer, VerticalContainer
from cassopi.ui.parser import parse_ui, parse_vertical_container
from cassopi.utils.yaml.parser import read_yaml

minimal_structure = '''
vertical_container:
'''

def test_parse_minimal_vertical_container():
    content = read_yaml(minimal_structure)
    root = content['vertical_container']
    vertical_container = parse_vertical_container(root)
    
    assert isinstance(vertical_container, VerticalContainer)

def test_read_minimal_ui_hierarchy():
    root = parse_ui(minimal_structure)
    
    assert root is not None
    assert isinstance(root, VerticalContainer)

structure_with_padding_in_all_directions = '''
vertical_container:
    padding:
        top: 5
        left: 10
        right: 15
        bottom: 20
'''

def test_parse_vertical_container_with_padding():
    content = read_yaml(structure_with_padding_in_all_directions)
    root = content['vertical_container']
    vertical_container = parse_vertical_container(root)
    
    assert isinstance(vertical_container, VerticalContainer)
    assert vertical_container.padding.top == 5
    assert vertical_container.padding.left == 10
    assert vertical_container.padding.right == 15
    assert vertical_container.padding.bottom == 20

def test_read_ui_hierarchy_with_padding_in_all_directions():
    root = parse_ui(structure_with_padding_in_all_directions)
    
    assert isinstance(root, VerticalContainer)
    assert root.padding.top == 5
    assert root.padding.left == 10
    assert root.padding.right == 15
    assert root.padding.bottom == 20

structure_with_all_padding = '''
vertical_container:
    padding:
        all: 10
'''

def test_parse_vertical_container_with_all_padding():
    content = read_yaml(structure_with_all_padding)
    root = content['vertical_container']
    vertical_container = parse_vertical_container(root)
    
    assert isinstance(vertical_container, VerticalContainer)
    assert vertical_container.padding.top == 10
    assert vertical_container.padding.left == 10
    assert vertical_container.padding.right == 10
    assert vertical_container.padding.bottom == 10

def test_read_ui_hierarchy_with_all_padding():
    root = parse_ui(structure_with_all_padding)
    
    assert isinstance(root, VerticalContainer)
    assert root.padding.top == 10
    assert root.padding.left == 10
    assert root.padding.right == 10
    assert root.padding.bottom == 10

structure_with_another_vertical_container = '''
vertical_container:
    padding:
        all: 10
    contains:
        - vertical_container:
            padding:
                right: 15
                left: 5
'''

def test_read_ui_hierarchy_with_contains():
    root = parse_ui(structure_with_another_vertical_container)
    
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
vertical_container:
    padding:
        all: 10
    contains:
        - horizontal_container:
            padding:
                right: 5
                top: 50
'''

def test_read_ui_hierarchy_with_contains_and_horizontal_container():
    root = parse_ui(structure_with_another_horizontal_container)
    
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
vertical_container:
    padding:
        all: 10
    contains:
        - horizontal_container:
            padding:
                right: 25
                top: 5
        - vertical_container:
            padding:
                left: 20
                right: 5
'''

def test_read_ui_hierarchy_with_multiple_containers():
    root = parse_ui(structure_with_multiple_containers)
    
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
