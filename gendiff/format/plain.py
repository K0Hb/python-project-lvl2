from gendiff.status_constants import (
    ADDED,
    REMOVED,
    NESTED,
    UNCHANGED,
)


def to_plain(difference, key_path=None):  # noqa: C901
    diff = []

    if not key_path:
        key_path = []

    for key, value in sorted(difference.items()):
        flag, rest = value[0], value[1:]
        if flag == UNCHANGED:
            continue
        elif flag == ADDED:
            add_added_node(key, diff, key_path, rest)
        elif flag == REMOVED:
            add_removed_node(key, diff, key_path, rest=None)
        elif flag == NESTED:
            add_nested_node(key, diff, key_path, rest)
        else:
            add_changed_node(key, diff, key_path, rest)
    return '\n'.join(diff)


def add_added_node(key, diff, key_path, rest):
    key_path.append(key)
    diff.append(
        'Property \'{0}\' was added with value: {1}'.format(
            '.'.join(key_path), render_value(rest[0])
        )
    )
    key_path.pop()


def add_removed_node(key, diff, key_path, rest=None):
    key_path.append(key)
    diff.append(
        'Property \'{}\' was removed'.format(
            '.'.join(key_path)
        )
    )
    key_path.pop()


def add_changed_node(key, diff, key_path, rest):
    key_path.append(key)
    diff.append(
        'Property \'{0}\' was updated. From {1} to {2}'.format(
            '.'.join(key_path), render_value(rest[0]),
            render_value(rest[1])
        )
    )
    key_path.pop()


def add_nested_node(key, diff, key_path, rest):
    key_path.append(key)
    diff.append(to_plain(rest[0], key_path))
    key_path.pop()


def render_value(value):
    if isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f'\'{value}\''
    else:
        return value
