import argparse
import os
import json
import yaml


def cli_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output (default: stylish)')
    return parser.parse_args()


def parse_file(file_path):
    format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }
    file_format = os.path.splitext(file_path)[1]
    with open(os.path.abspath(file_path)) as f:
        return format[file_format](f.read())
