#!/usr/bin/python3
"""Defines a string-to-JSON function."""
from json import dumps


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return dumps(my_obj)
