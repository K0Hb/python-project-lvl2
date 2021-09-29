from gendiff.parser_files import get_parser_file
from gendiff.format.get_format import get_formatter
from gendiff.status_constants import (
    ADDED,
    CHANGED,
    REMOVED,
    NESTED,
    UNCHANGED,
)


def build_diff(old, new):
    diff = {}

    removed_keys = old.keys() - new.keys()
    for key in (removed_keys):
        diff[key] = [REMOVED, old.get(key)]
    added_keys = new.keys() - old.keys()
    for key in (added_keys):
        diff[key] = [ADDED, new.get(key)]
    for key in (old.keys() & new.keys()):
        old_value = old.get(key)
        new_value = new.get(key)
        has_children = (
            isinstance(old_value, dict)
        ) and (
            isinstance(new_value, dict)
        )
        if has_children and old_value != new_value:
            diff[key] = [NESTED, build_diff(old_value, new_value)]
        elif old_value == new_value:
            diff[key] = [UNCHANGED, new_value]
        else:
            diff[key] = [CHANGED, old_value, new_value]
    return diff


def generate_diff(path_file1, path_file2, output_format='stylish'):
    diff = build_diff(get_parser_file(path_file1), get_parser_file(path_file2))
    return get_formatter(output_format)(diff)
