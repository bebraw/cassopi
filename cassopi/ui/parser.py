from containers import VerticalContainer
from cassopi.utils.yaml.parser import read_yaml

class StructureParser():
    def __init__(self, structure):
        self.content = read_yaml(structure)
    
    def parse(self):
        return globals()[self.content.keys()[0]](args=self.content.values()[0])
