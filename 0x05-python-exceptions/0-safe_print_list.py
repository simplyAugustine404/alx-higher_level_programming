#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ans = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            ans += 1
        print()
        return ans
    except IndexError:
        print()
        return ans
