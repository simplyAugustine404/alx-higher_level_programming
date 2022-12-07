#!/usr/bin/python3
"""prints numbers 0-98 in decimal and hex"""

for number in range(99):
    print("{:d} = 0x{:x}".format(number, number))
