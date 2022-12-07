#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    lst = sys.argv[1:]
    result = 0
    for i in lst:
        result += int(i)
    print(f"{result:d}")
