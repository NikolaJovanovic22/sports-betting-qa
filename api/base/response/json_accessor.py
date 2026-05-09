from typing import Any


def get_by_path(data: Any, path: str, default=None):
    value = data

    for key in path.split("."):
        # list access
        if isinstance(value, list):
            if not key.isdigit():
                return default
            idx = int(key)
            if idx >= len(value):
                return default
            value = value[idx]

        # dict access
        elif isinstance(value, dict):
            if key not in value:
                return default
            value = value[key]

        else:
            return default

    return value
