#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    ans = 0
    for i in roman_string:
        if i == "I":
            ans += 1
        elif i == "V":
            ans += 5
        elif i == "X":
            ans += 10
        elif i == "L":
            ans += 50
        elif i == "C":
            ans += 100
        elif i == "D":
            ans += 500
        elif i == "M":
            ans += 1000
        else:
            return None
