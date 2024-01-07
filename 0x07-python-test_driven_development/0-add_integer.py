#!/usr/bin/python3
'''
    Module add integer
    Adds two integers
'''



def add_integer(a: int| float, b=98)-> int:
    '''Returns an integer: the addition of a and b
        where a and b is of type float or int
    '''
    add_sum = 0
    for x in (a,b):
        if type(x) is not int and type(x) is not float:
            raise TypeError(f'{"a" if x == a else "b"} must be an integer')
        if type(x) is float:
            x = int(x)
        add_sum += x
    return (add_sum)


