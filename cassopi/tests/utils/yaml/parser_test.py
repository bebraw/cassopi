from cassopi.utils.yaml.parser import read_yaml

test_structure = '''
- some_item:
'''

def test_read_invalid_file():
    file_content = read_yaml('foo.yaml')
    assert file_content is None

def test_read_valid_file():
    file_content = read_yaml('valid.yaml') # put in proper place and fix path!  
    assert file_content is not None

def test_read_non_file_structure():
    structure_content = read_yaml(test_structure)
    assert structure_content is not None
