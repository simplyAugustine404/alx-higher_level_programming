#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div
    v = sys.argv[1:]
    if len(v) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(v[0])
    operator = v[1]
    b = int(v[2])

    if operator == '+':
        print(f"{a:d} {operator} {b:d} = {add(a, b):d}")
    elif operator == '-':
        print(f"{a:d} {operator} {b:d} = {sub(a, b):d}")
    elif operator == '*':
        print(f"{a:d} {operator} {b:d} = {mul(a, b):d}")
    elif operator == '/':
        print(f"{a:b} {operator} {b:d} = {div(a, b):d}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
