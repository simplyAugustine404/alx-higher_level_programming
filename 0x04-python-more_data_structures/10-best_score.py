#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    val = max(list(a_dictionary.values()))
    for i, j in zip(a_dictionary.keys(), a_dictionary.values()):
        if j == val:
            return i
    return None
