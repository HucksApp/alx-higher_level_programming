#!/usr/bin/python3

def upperchar(c: str) -> int:
    asc = (ord(c) - 32) if (ord(c) >= 97 and ord(c) <= 122) else ord(c)
    return asc


def uppercase(str: str) -> None:
    ret = ""
    for chars in str:
        ret += "%c" % upperchar(chars)
    print("{:s}".format(ret))
