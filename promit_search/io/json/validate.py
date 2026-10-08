

from pathlib import Path
import json


def _keys_match(data: dict, template: dict) -> bool:
    """Recursively check that data has exactly the keys in template.

    Where the template value is itself a dict, the matching value in data
    must also be a dict with matching keys.
    """
    if not isinstance(data, dict) or not set(template).issubset(set(data)):
        return False
    for key, template_value in template.items():
        if isinstance(template_value, dict) and not _keys_match(data[key], template_value):
            return False
    return True


def validate(json_file: Path, keys_dict: dict) -> bool:
    """Takes in a JSON file and validates it by checking
    keys in input dictionary match that in JSON

    Args:
        json_file: JSON to validate
        keys_dict: dictionary that has format of valid json_file

    Returns:
        True if the JSON's keys match keys_dict, False otherwise

    Raises:
        ValueError: if the file cannot be read or is not valid JSON
    """
    try:
        with open(json_file) as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        raise ValueError("Invalid JSON file {}: {}".format(json_file, e)) from e

    if _keys_match(data, keys_dict):
        return True
    else:
        raise ValueError("JSON file {} does not match format".format(json_file))

    