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


def parse_file(file_path):
    file_format = os.path.splitext(file_path)[1]
    with open(os.path.abspath(file_path)) as f:
        return parser(file_format)(f.read())
