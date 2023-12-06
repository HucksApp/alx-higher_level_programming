#!/usr/bin/python3
def simple_delete(a_dictionary: dict, key: str = "") -> dict:
    if key:
        a_dictionary.pop(key)
    return a_dictionary
