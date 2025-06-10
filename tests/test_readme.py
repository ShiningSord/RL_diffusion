import pathlib

def test_dataset_name():
    text = pathlib.Path('README.md').read_text()
    assert 'compressed_animals' in text
