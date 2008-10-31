from paddings import Padding
from containers import HorizontalContainer, VerticalContainer
from cassopi.utils.yaml.parser import read_yaml

class StructureParser():
    def __init__(self, structure):
        content = read_yaml(structure)
        self.content_root = content['VerticalContainer']
    
    def parse(self):
        return globals()['VerticalContainer'](args=self.content_root)
