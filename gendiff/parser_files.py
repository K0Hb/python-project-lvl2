import os
import json
import yaml


def parse_file(file_path):
    format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }
    file_format = os.path.splitext(file_path)[1]
    with open(os.path.abspath(file_path)) as f:
        return format[file_format](f.read())
