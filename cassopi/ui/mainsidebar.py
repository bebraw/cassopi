# -*- coding: utf-8 -*-
"""
Main sidebar of whole screen.
"""
from elements.button import Button
from elements.element import Element
from elements.tab import Tab
from sidebar import Sidebar
from tabmanager import TabManager

class MainSidebar(Sidebar):
    def __init__(self):
        self.tab_manager = TabManager()
        
        # ElementGroup ???
        main_tab = Tab('Main')
        main_tab.add(Button('New', None)) # attach events too! None -> func
        main_tab.add(Button('Open')) # make this foldable instead? Folder()
        main_tab.add(Element())
        main_tab.add(Button('Save'))
        main_tab.add(Button('Save as...'))
        main_tab.add(Element())
        main_tab.add(Button('Quit'))
        
        settings_tab = Tab('Settings')
        settings_tab.add(Button('Some setting'))
        
        self.tab_manager.add(main_tab)
        self.tab_manager.add(settings_tab)
    
    def render(self):
        self.tab_manager.render()
