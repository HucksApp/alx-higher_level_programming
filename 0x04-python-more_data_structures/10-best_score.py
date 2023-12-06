#!/usr/bin/python3
def best_score(a_dictionary: dict) -> str:
    bst, bst_key = 0, ""
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > bst:
                bst = value
                bst_key = key
        return bst_key
    return None
