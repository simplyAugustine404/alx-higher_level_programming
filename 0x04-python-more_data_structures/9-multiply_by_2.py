#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ans = {}
    for i, j in a_dictionary.items():
        ans[i] = j * 2
    return ans
