import os
import re


def evaluate_simple(expr):
    while '+' in expr:
        expr = addR.sub(lambda m: str(int(m[1]) + int(m[2])), expr)

    tokens = expr.split(' * ')

    prod = 1
    for num in tokens:
        prod *= int(num)
    return prod


def evaluate_expr(line):
    while True:
        line, n = parentR.subn(lambda m: str(evaluate_simple(m[1])), line)
        if n == 0:
            break
    return evaluate_simple(line)


parentR = re.compile(r'\(([^()]+)\)')
addR = re.compile(r'(\d+) \+ (\d+)')
result = 0

with open(os.path.join('data', 'aoc18.txt')) as f:
    for line in f:
        result += evaluate_expr(line.rstrip())

print(result)
