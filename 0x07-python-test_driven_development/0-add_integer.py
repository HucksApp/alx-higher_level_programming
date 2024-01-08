#!/usr/bin/python3
"""
Module add-integer
Adds two integer together

"""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b
    where a and b is of type float or int
    """

    add_sum = 0
    for x in (a, b):
        if type(x) not in [float, int]:
            raise TypeError(f'{"a" if x == a else "b"} must be an integer')
        if type(x) is float:
            x = int(x)
        add_sum += x
    return (add_sum)
