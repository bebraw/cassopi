# -*- coding: utf-8 -*-
from cassopi.ui.paddings import Padding
from cassopi.ui.uicontainers import VerticalContainer

def test_create_VerticalContainer():
    vertical_container = VerticalContainer()
    
    assert isinstance(vertical_container, VerticalContainer)

def test_create_VerticalContainer_with_padding():
    padding = Padding()
    vertical_container = VerticalContainer(padding=padding)
    
    assert isinstance(vertical_container, VerticalContainer)
    assert isinstance(vertical_container.padding, Padding)
