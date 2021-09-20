from gendiff.parser_files import parse_file
from gendiff import format
from gendiff.library import ADDED, CHANGED, REMOVED, NESTED, UNCHANGED


def build_diff(old, new):
    diff = {}
    removed_keys = old.keys() - new.keys()
    diff.update(
        {
            key: (REMOVED, old.get(key))
            for key in sorted(removed_keys)
        }
    )
    added_keys = new.keys() - old.keys()
    diff.update(
        {
            key: (ADDED, new.get(key))
            for key in sorted(added_keys)
        }
    )
    for key in sorted(old.keys() & new.keys()):
        old_value = old.get(key)
        new_value = new.get(key)
        has_children = (
            isinstance(old_value, dict)
        ) and (
            isinstance(new_value, dict)
        )
        if has_children:
            diff[key] = (NESTED, build_diff(old_value, new_value))
        elif old_value == new_value:
            diff[key] = (UNCHANGED, new_value)
        else:
            diff[key] = (CHANGED, old_value, new_value)
    return diff


def formatter(string_format):
    formats = {
        'stylish': format.stylish,
        'plain': format.plain,
        'json': format.json
    }
    return formats[string_format]


def generate_diff(old, new, output_format='stylish'):
    diff = build_diff(parse_file(old), parse_file(new))
    return formatter(output_format)(diff)
