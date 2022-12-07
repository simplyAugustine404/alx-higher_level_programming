#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    for i, c in enumerate(str, start=0):
        if i == n:
            continue
        else:
            cpy += c
    return (cpy)
