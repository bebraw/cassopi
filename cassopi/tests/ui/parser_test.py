# -*- coding: utf-8 -*-
from cassopi.ui.containers import VerticalContainer
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
    file_content = parse_ui(minimal_structure)
    
    assert file_content is not None
    assert isinstance(file_content, VerticalContainer)

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
    file_content = parse_ui(structure_with_padding_in_all_directions)
    
    assert file_content is not None
    assert isinstance(file_content, VerticalContainer)
    assert file_content.padding.top == 5
    assert file_content.padding.left == 10
    assert file_content.padding.right == 15
    assert file_content.padding.bottom == 20

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
    file_content = parse_ui(structure_with_all_padding)
    assert file_content is not None
    assert isinstance(file_content, VerticalContainer)
    assert file_content.padding.top == 10
    assert file_content.padding.left == 10
    assert file_content.padding.right == 10
    assert file_content.padding.bottom == 10
