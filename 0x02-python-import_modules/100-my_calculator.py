#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    num_args = len(sys.argv)
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator is "+":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator is "-":
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator is "*":
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif operator is "/":
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
