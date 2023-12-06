#!/usr/bin/python3
def common_elements(set_1, set_2):
    com_set = []
    for x in set_1:
        for y in set_2:
            if x == y:
                com_set.append(x)
    return com_set
