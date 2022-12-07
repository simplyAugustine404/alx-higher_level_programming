#!/usr/bin/python3
"""Print the alphabet, except e and q"""

for letter in range(97, 123):
    if letter == 101 or letter == 113:
        continue
    else:
        print("{}".format(chr(letter)), end="")
