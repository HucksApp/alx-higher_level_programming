#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set = [*set([*set_1, *set_2])]
    for elem_a in [*set_1]:
        for elem_b in [*set_2]:
            if elem_a == elem_b:
                diff_set.remove(elem_a)
    return diff_set
