#!/usr/bin/python3
"""Defines a JSON-to-object function."""
from json import loads


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return loads(my_str)
