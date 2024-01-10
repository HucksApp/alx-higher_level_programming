#!/usr/bin/python3
"""Defines a JSON file-writing function."""
from json import dump


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        dump(my_obj, f)
