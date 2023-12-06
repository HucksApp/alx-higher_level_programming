#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary: dict) -> None:
    for key, value in sorted([*a_dictionary.items()]):
        print(f"{key}: {value}")
