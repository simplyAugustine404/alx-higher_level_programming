#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}", value)
        return True
    except ValueError:
        return False