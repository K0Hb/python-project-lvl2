import os
import json
import yaml


def parser(file_format):
    format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }
    return format[file_format.lower()]


def get_parser_file(file_path):
    file_format = get_format(file_path)
    file = open_file(file_path)
    return parser(file_format)(file)


def get_format(file_path):
    file_format = os.path.splitext(file_path)[1]
    return file_format


def open_file(file_path):
    with open(os.path.abspath(file_path)) as f:
        file = f.read()
    return file
