# -*- coding: utf-8 -*-

def generate_random_color(variance=128, offset=128):
    color = []
    
    for col in range(3):
        val = int(random() * variance + offset)
        color.append(clamp(val, 0, 255))
    
    return color
