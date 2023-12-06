#!/usr/bin/python3
def number_keys(a_dictionary: dict) -> int:
    keys = [key for key in a_dictionary.keys()]
    return len(keys)
