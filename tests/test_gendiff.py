import pytest
from gendiff.scripts.gendiff import generate_diff
import os


def get_fixtures_data(file_name):
    path_to_file = os.path.join('tests/fixtures', file_name)
    with open(path_to_file, 'r') as f:
        return f.read()


def test_generate_diff():
    result = generate_diff(get_fixtures_data('file1.json'), get_fixtures_data('file2.json'))
    expected = get_fixtures_data('result_flat')
    assert result == expected