from gendiff import format


def formatter(string_format):
    formats = {
        'stylish': format.stylish,
        'plain': format.plain,
        'json': format.json
    }
    return formats[string_format]
