import json


def sortik(diff):
    result = {}
    diffik = sorted(diff.keys())
    for key in diffik:
        result[key] = diff[key]
        if isinstance(diff[key], list):
            if isinstance(diff[key][1], dict):
                result[key][1] = sortik(diff[key][1])
    return result


def to_json(diff):
    return json.dumps(sortik(diff), indent=2)
