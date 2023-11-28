#!/usr/bin/python3

def print_last_digit(number: int) -> int:
    last = number % 10 if (number >= 0) else (number % -10) * -1
    print("{:d}".format(last), end='')
    return last
