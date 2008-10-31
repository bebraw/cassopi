# -*- coding: utf-8 -*-
from cassopi.ui.paddings import Padding
from cassopi.ui.containers import HorizontalContainer, VerticalContainer

def test_create_VerticalContainer():
    vertical_container = VerticalContainer()
    
    assert isinstance(vertical_container, VerticalContainer)

def test_create_VerticalContainer_with_padding():
    padding = Padding()
    vertical_container = VerticalContainer(padding=padding)
    
    assert isinstance(vertical_container, VerticalContainer)
    assert isinstance(vertical_container.padding, Padding)

def test_add_child_to_VerticalContainer():
    vertical_container = VerticalContainer()
    vertical_container2 = VerticalContainer()
    
    vertical_container.children.append(vertical_container2)
    
    vertical_container_child = vertical_container.children[0]
    
    assert vertical_container_child is vertical_container2

def test_create_HorizontalContainer():
    horizontal_container = HorizontalContainer()
    
    assert isinstance(horizontal_container, HorizontalContainer)

def test_create_HorizontalContainer_with_padding():
    padding = Padding()
    horizontal_container = HorizontalContainer(padding=padding)
    
    assert isinstance(horizontal_container, HorizontalContainer)
    assert isinstance(horizontal_container.padding, Padding)

def test_add_child_to_HorizontalContainer():
    horizontal_container = HorizontalContainer()
    horizontal_container2 = HorizontalContainer()
    
    horizontal_container.children.append(horizontal_container2)
    
    horizontal_container_child = horizontal_container.children[0]
    
    assert horizontal_container_child is horizontal_container2
