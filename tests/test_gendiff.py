import os
import pytest
from gendiff.gendiff_base import generate_diff


def locate(file, status):
    status_dict = {
        'before': 'files_before',
        'after': 'files_after',
        'result': 'files_result'
    }
    return os.path.join('tests', 'fixtures', status_dict[status], file)


def diff_result(output_format):
    return generate_diff(
        locate('file_before.json', 'before'),
        locate('file_after.json', 'after'),
        output_format
    )


@pytest.mark.parametrize('path_fixture, status, format', [
    ('expected_stylish.txt', 'result', 'stylish'),
    ('expected_plain.txt', 'result', 'plain'),
    ('expected_json.txt', 'result', 'json'),
])
def test_generate_diff(path_fixture, status, format):
    with open(locate(path_fixture, status)) as f:
        expected = f.read().strip()
        print(diff_result(format))
    assert diff_result(format) == expected
