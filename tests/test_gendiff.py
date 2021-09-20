import os
import json
import pytest
from gendiff.gendiff_base import generate_diff, build_diff
from gendiff.parser import parse_file


def locate(file):
    return os.path.join('tests', 'fixtures', file)


def diff_result(output_format):
    return generate_diff(
        locate('file_before.json'),
        locate('file_after.json'),
        output_format
    )


@pytest.mark.parametrize('path_fixture, format', [
    ('expected_stylish.txt', 'stylish'),
    ('expected_plain.txt', 'plain'),
    ('expected_json.txt', 'json'),
])
def test_generate_diff(path_fixture, format):
    with open(locate(path_fixture)) as f:
        expected = f.read().strip()
    assert diff_result(format) == expected


def test_build_diff():
    old_dict = parse_file(locate('file_before.json'))
    new_dict = parse_file(locate('file_after.json'))
    with open(locate('build_diff.txt')) as f:
        expected = f.read().strip()
    assert json.dumps(build_diff(old_dict, new_dict)) == expected
