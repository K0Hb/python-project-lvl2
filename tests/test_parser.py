from gendiff.parser_files import get_parser_file
from test_gendiff import locate


def test_file_parser():
    output = get_parser_file(locate('file1.yml', 'before')), get_parser_file(locate('file2.yaml', 'after'))
    with open(locate('file_parser_output.txt', 'result')) as f:
        expected = f.read().strip()
        assert f'{output}' == expected
