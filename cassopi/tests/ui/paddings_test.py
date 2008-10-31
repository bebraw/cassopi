# -*- coding: utf-8 -*-
from cassopi.ui.paddings import Padding

def test_create_empty_padding():
    padding = Padding()
    
    assert isinstance(padding, Padding)
    assert padding.top == 0
    assert padding.left == 0
    assert padding.right == 0
    assert padding.bottom == 0

def test_create_padding_with_values():
    padding = Padding(top=10, right=5, bottom=20, left=15)
    
    assert isinstance(padding, Padding)
    assert padding.top == 10
    assert padding.left == 15
    assert padding.right == 5
    assert padding.bottom == 20

def test_create_padding_with_invalid_values():
    padding = Padding(top=-10, right=-5, bottom=-20, left=-15)
    
    assert isinstance(padding, Padding)
    assert padding.top == 0
    assert padding.left == 0
    assert padding.right == 0
    assert padding.bottom == 0

def test_create_padding_with_dictionary():
    padding = Padding(**{'top': 5, 'right': 10, })
    
    assert isinstance(padding, Padding)
    assert padding.top == 5
    assert padding.right == 10

def test_create_padding_with_all():
    padding = Padding(**{'all': 10})
    
    assert isinstance(padding, Padding)
    assert padding.top == 10
    assert padding.left == 10
    assert padding.right == 10
    assert padding.bottom == 10
