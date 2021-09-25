from gendiff.parser_files import parse_file
from gendiff.format.get_format import formatter
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
    for key in sorted(removed_keys):
        diff[key] = (REMOVED, old.get(key))
    added_keys = new.keys() - old.keys()
    for key in sorted(added_keys):
        diff[key] = (ADDED, new.get(key))
    for key in sorted(old.keys() & new.keys()):
        old_value = old.get(key)
        new_value = new.get(key)
        has_children = (
            isinstance(old_value, dict)
        ) and (
            isinstance(new_value, dict)
        )
        if has_children and old_value != new_value:
            diff[key] = (NESTED, build_diff(old_value, new_value))
        elif old_value == new_value:
            diff[key] = (UNCHANGED, new_value)
        else:
            diff[key] = (CHANGED, old_value, new_value)
    return diff


def generate_diff(old, new, output_format='stylish'):
    diff = build_diff(parse_file(old), parse_file(new))
    return formatter(output_format)(diff)
